from collections import defaultdict
from datetime import datetime, timedelta
from itertools import islice
from traceback import print_exception

from datetimerange import DateTimeRange
from discord import TextChannel
from discord.ext import commands, tasks
from pytz import timezone
from timefhuman import timefhuman

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
        channel_id = 666716587083956224
        send = self.scheduler.bot.get_channel(channel_id).send
        event_id = 712784506624540713
        await self.scheduler.send_when(send, 0, 1.5, event_id)
        return proto.hermes_pb2.Empty()


class Scheduler(commands.Cog):
    """A discord.py Cog to collect and interpret times that users are free to help schedule an event"""

    def __init__(self, bot):
        self.bot = bot
        self.db = PlayerDB()
        self.whens = {}

        grpc.experimental.aio.init_grpc_aio()
        self.server = grpc.experimental.aio.server()
        proto.hermes_pb2_grpc.add_SchedulerServicer_to_server(SchedulerGrpc(self), self.server)
        self.server.add_insecure_port('[::]:8080')
        self.start_grpc.start()

        self.generate_whens.start()

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

    @tasks.loop(seconds=10)
    async def generate_whens(self):

        for channel in self.bot.get_all_channels():

            if not isinstance(channel, TextChannel):
                continue
            
            try: 
                player_timeranges = self.db.get_players(channel.id).items()
            except KeyError:
                continue
            
            whens = []
            for n in range(5, 0, -1):

                result = defaultdict(list)
                for player, timeranges in player_timeranges:
                    for timerange in timeranges:
                        result[player].append(timerange.datetimerange())

                result = find_times(result, n)
                result = deduplicate_times(result)

                if result:
                    whens.append((n, result))

            self.whens[channel.id] = whens
        
        return self.whens


    @commands.command()
    async def when(self, ctx, people=None, duration=1.5, event=None):
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
            Default: 1.5
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
        event_id = await self.get_event_id(ctx, event)
        await self.send_when(ctx.send, int(people), float(duration), event_id)
    
    async def send_when(self, send, people, duration, event_id):
        if people == 66:
            await send(SIXTY_SIX)

        results = self.whens[event_id]

        if not people:

            msg = [f"found times for **{results[0][0]}** players for ⩾**{duration}**h:\n\n"]
            for players, times in filter_times(results[0][1], duration).items():
                msg.append(f"_{', '.join(players)}_ at:\n")
                msg.extend(format_datetimeranges(times))
                msg.append("\n")

            return await send("".join(msg))

        for result in results:

            if result[0] == people:

                msg = [f"found times for ⩾**{result[0]}** players for ⩾**{duration}**h:\n\n"]
                for players, times in filter_times(result[1], duration).items():
                    msg.append(f"_{', '.join(players)}_ at:\n")
                    msg.extend(format_datetimeranges(times))
                    msg.append("\n")

                return await send("".join(msg))

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
        event_id = await self.get_event_id(ctx, event)
        players = self.db.get_players(event_id)

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

    async def get_event_id(self, ctx, event):
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
