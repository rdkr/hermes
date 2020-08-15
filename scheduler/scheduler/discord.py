from collections import defaultdict
from datetime import datetime, timedelta
from itertools import islice
import logging
from traceback import print_exception

from datetimerange import DateTimeRange
from discord import TextChannel, Embed
from discord.ext import commands, tasks
from discord.errors import NotFound
from pytz import timezone

from scheduler.formatting import format_datetimeranges, format_timeranges, format_range
from scheduler.sql import PlayerDB
from scheduler.scheduler import filter_times, find_times, deduplicate_times

SIXTY_SIX = "https://pa1.narvii.com/7235/5ceb289c2b7953a679dafaf9fc7f4f6ab0afc394r1-480-208_hq.gif"

import grpc.experimental.aio
import proto.hermes_pb2
import proto.hermes_pb2_grpc

from discord.ext import tasks, commands


class SchedulerGrpc(proto.hermes_pb2_grpc.SchedulerServicer):
    def __init__(self, scheduler):
        self.scheduler = scheduler

    async def NotifyUpdated(self, request, context):
        try:
            # first entry or None if empty list
            previous_when = next(iter(self.scheduler.whens[request.id]), None)
            logging.info(f"previous: {previous_when}")

            # generate new whens
            self.scheduler.whens[
                request.id
            ] = await self.scheduler.generate_whens_for_channel(request.id)
            new_when = next(iter(self.scheduler.whens[request.id]), None)
            logging.info(f"new: {new_when}")

            # compare whens and send msg if changed
            if not str(previous_when) == str(new_when):
                channel_id = self.scheduler.db.event_id_to_event_dc_id(request.id)
                channel = self.scheduler.bot.get_channel(int(channel_id))

                whens = self.scheduler.whens[request.id]
                when = next(iter(whens), None)

                await self.scheduler.send_when(
                    channel, when, self.scheduler.whens_min_time[request.id]
                )

            return proto.hermes_pb2.Empty()
        except Exception as e:
            logging.error(e)
            import traceback

            traceback.print_exc()


class Scheduler(commands.Cog):
    """A discord.py Cog to collect and interpret times that users are free to help schedule an event"""

    def __init__(self, bot):
        self.bot = bot
        self.db = PlayerDB()
        self.whens_min_time = {}
        self.whens = {}

        grpc.experimental.aio.init_grpc_aio()
        self.server = grpc.experimental.aio.server()
        proto.hermes_pb2_grpc.add_SchedulerServicer_to_server(
            SchedulerGrpc(self), self.server
        )
        self.server.add_insecure_port("[::]:8081")
        self.start_grpc.start()

        self.generate_whens_loop.start()

    @tasks.loop(count=1)
    async def start_grpc(self):
        await self.server.start()

    @commands.Cog.listener()
    async def on_error(self, event):
        print(event)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        print_exception(type(exception), exception, exception.__traceback__)
        await ctx.send(f"error!")

    @tasks.loop(seconds=60)
    async def generate_whens_loop(self):
        for event in self.db.get_events():
            self.whens_min_time[event.event_id] = event.min_time
            self.whens[event.event_id] = await self.generate_whens_for_channel(
                event.event_id
            )

    async def generate_whens_for_channel(self, event_id, duration=None):

        if not duration:
            duration = self.whens_min_time[event_id]

        try:
            player_timeranges = self.db.get_players(event_id).items()
        except KeyError:
            return []

        whens = []
        for n in range(6, 0, -1):

            result = defaultdict(list)
            for player, timeranges in player_timeranges:
                for timerange in timeranges:
                    result[player].append(timerange.datetimerange())

            result = find_times(result, n)
            result = deduplicate_times(result)
            result = filter_times(result, duration)

            if result:
                whens.append((n, result))

        return whens

    @commands.command()
    async def when(self, ctx, people=None, duration=None, event=None):
        """Find times for an event.

        With no arguments, this will return the timeranges during which
        the most people are available for at least 1.5 hours.

        Arguments can be provided to cause the timeranges to be for at
        least a given number of people for at least a given duration.

        Parameters
        ----------
        people
            Optional: the number of people who need to be available
            Default: 0 (implies maximum possible)
        duration
            Optional: the minimum duration in hours for the event
            Default: the events default
        event
            Optional: the name of the event channel to calculate for
            Default: current channel

        Examples
        --------
          - $when
          - $when 3
          - $when 0 2
          - $when 3 2 dnd
        """
        event_dc_id = await self.get_event_dc_id(ctx, event)
        event_id = self.db.event_dc_id_to_event_id(event_dc_id)

        if (not people or not int(people)) and (not duration or not int(duration)):
            if not people:
                people = 0

            whens = self.whens[event_id]
            when = next(iter(whens), None)

            await self.send_when(ctx.channel, when, self.whens_min_time[event_id])

        else:
            if not duration:
                duration = self.whens_min_time[event_id]
            if int(people) < 0:
                raise ValueError

            # if people == "66": # todo re-enable memes - seems the update broke gif embed
            #     await ctx.send(embed=Embed(url=SIXTY_SIX))

            keep_msg = await ctx.send(
                f"calculating times for ⩾**{people}** players for ⩾**{float(duration)}**h..."
            )

            whens = await self.generate_whens_for_channel(event_id, float(duration))

            when = None
            for check_when in whens:
                if check_when[0] == int(people):
                    when = check_when
                    break

            await self.send_when(ctx.channel, when, float(duration), [keep_msg.id])

    async def send_when(self, channel, when, duration, keep_msgs=None):

        if when:
            embed = Embed(
                title="Availability",
                description=f"for **{when[0]}** players for ⩾**{duration}**h",
                color=0x00FF00,
            )

            for players, times in when[1].items():
                embed.add_field(
                    name=", ".join(sorted(list(players))),
                    value="".join(format_datetimeranges(times)),
                    inline=False,
                )

        else:
            embed = Embed(
                title="Availability",
                description=f"none for ⩾**{duration}**h",
                color=0xFF0000,
            )

        msg = await channel.send(embed=embed)

        try:

            def check_msg(message):

                author_check = message.author == self.bot.user
                last_msg_check = msg.id != message.id

                if keep_msgs:
                    keep_msg_check = message.id not in keep_msgs
                else:
                    keep_msg_check = True

                return author_check and last_msg_check and keep_msg_check

            await channel.purge(check=check_msg)
        except NotFound as e:
            print(e)

    @commands.command(hidden=True)
    async def list(self, ctx, who=None, event=None):
        """List when you or others are marked as free.

        Parameters
        ----------
        who
            Optional: the Discord name of the user to list, or "all"
            Default: you
        event
            Optional: the name of the event channel to list for
            Default: current channel

        Examples
        --------
          - $list
          - $list Jon
          - $list all
          - $list Jon dnd
          - $list all dnd
        """
        event_dc_id = await self.get_event_dc_id(ctx, event)
        players = self.db.get_players(self.db.event_dc_id_to_event_id(event_dc_id))

        if not who:
            who = [ctx.message.author.name]
        elif who == "all":
            who = players.keys()
        else:
            who = [who]

        for player in who:
            for chunk in chunks(players[player], 10):
                msg = [f"possible times:\n\n"]
                msg.append(f"_{player}_ at:\n")
                msg.extend(format_timeranges(chunk))
                msg.append("\n")
                await ctx.send("".join(msg))

    @commands.command()
    async def login(self, ctx):
        """Get a magic link to the web interface via DM.
        """
        warning = (
            "⚠️ this is a magic link which logs in to your account, **don't share it**!"
        )
        link = f"<https://hermes.rdkr.uk/login?token={self.db.get_magic_token(ctx.message.author.id)}>"
        await ctx.message.author.send(f"{warning}\n\n{link}")

    @commands.command(hidden=True)
    async def sync(self, ctx):
        """Syncronise players from Discord to database.
        """
        self.run_sync()
        await ctx.message.author.send(f"sync complete")

    async def get_event_dc_id(self, ctx, event):
        if not event:
            return ctx.message.channel.id
        else:
            for channel in self.bot.get_all_channels():
                if (
                    isinstance(channel, TextChannel)
                    and channel.name == event
                    and ctx.message.author in channel.members
                ):
                    await ctx.send(
                        f"assuming channel: {channel.guild.name}/{channel.name} ({channel.id})"
                    )
                    return channel.id
        raise KeyError

    def run_sync(self):
        valid = set()
        for guild in self.bot.guilds:
            for channel in guild.channels:
                can_send = channel.permissions_for(guild.me).send_messages
                if isinstance(channel, TextChannel) and can_send:
                    for member in channel.members:
                        if not member == guild.me:
                            valid.add(
                                (
                                    channel.id,
                                    guild.name,
                                    channel.name,
                                    member.id,
                                    member.name,
                                )
                            )
        self.db.sync_event_players(valid)


def chunks(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())
