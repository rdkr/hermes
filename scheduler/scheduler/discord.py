from collections import defaultdict
import copy
from datetime import datetime, timedelta
from itertools import islice
import logging
from traceback import print_exception

from datetimerange import DateTimeRange
from discord import TextChannel, Embed
from discord.ext import commands, tasks
from discord.errors import NotFound
from pytz import timezone

from scheduler.formatting import (
    format_datetimeranges,
    format_timeranges,
    format_range,
    chunks,
)
from scheduler.db import PlayerDB
from scheduler.scheduler import filter_times, find_times, deduplicate_times

SIXTY_SIX = "https://pa1.narvii.com/7235/5ceb289c2b7953a679dafaf9fc7f4f6ab0afc394r1-480-208_hq.gif"


from discord.ext import tasks, commands


class Scheduler(commands.Cog):
    """A discord.py Cog to collect and interpret times that users are free to help schedule an event"""

    def __init__(self, bot):
        self.bot = bot
        self.db = PlayerDB()

        self.players = {}
        self.events = {}
        self.whens = {}

    @commands.Cog.listener()
    async def on_ready(self):
        await self.sync()
        self.generate_whens_loop.start()
        self.sync_loop.start()

    @commands.Cog.listener()
    async def on_error(self, event):
        print(event)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        print_exception(type(exception), exception, exception.__traceback__)
        await ctx.send(f"error!")

    @tasks.loop(seconds=30)
    async def sync_loop(self):
        await self.sync()

    async def sync(self):
        valid = []
        for guild in self.bot.guilds:
            for channel in guild.channels:
                can_send = channel.permissions_for(guild.me).send_messages
                if isinstance(channel, TextChannel) and can_send:
                    for member in channel.members:
                        if not member == guild.me:
                            valid.append(
                                dict(
                                    guild_name=guild.name,
                                    channel_id=str(channel.id),
                                    channel_name=channel.name,
                                    player_id=str(member.id),
                                    player_name=member.name,
                                )
                            )
                            self.players[str(member.id)] = member.name
        await self.db.sync_event_players(valid)

    @tasks.loop(seconds=5)
    async def generate_whens_loop(self):
        events = await self.db.get_events()
        self.events = {event.event_id: event for event in events}

        for event in self.events.values():

            new_whens = await self.generate_whens_for_channel(event.event_id)

            try:

                # this will give the first entry or [] if empty list
                previous_when = next(iter(self.whens[event.event_id]), [])

                if not str(self.whens[event.event_id]) == str(new_whens):

                    # deepcopy as dict is mutable # todo - not use dict
                    when = copy.deepcopy(next(iter(new_whens), []))

                    channel = self.bot.get_channel(int(event.event_dc_id))
                    await self.send_when(channel, when, event.min_time)

            except KeyError:
                pass  # expected at first start

            self.whens[event.event_id] = new_whens

    async def generate_whens_for_channel(self, event_id, duration=None):

        if not duration:
            duration = self.events[event_id].min_time

        player_timeranges = await self.db.get_players(event_id)

        whens = []
        for n in range(len(player_timeranges), 0, -1):

            result = find_times(player_timeranges, n)
            result = deduplicate_times(result)
            result = filter_times(result, duration)

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
        event_id = await self.event_dc_id_to_event_id(event_dc_id)

        if (not people or not int(people)) and (not duration or not int(duration)):
            if not people:
                people = 0

            whens = self.whens[event_id]
            # deepcopy as dict is mutable # todo - not use dict
            when = copy.deepcopy(next(iter(whens), []))

            await self.send_when(ctx.channel, when, self.events[event_id].min_time)

        else:
            if not duration:
                duration = self.events[event_id].min_time
            if int(people) < 0:
                raise ValueError

            keep_msgs = []

            keep_msgs.append(
                (
                    await ctx.send(
                        f"calculating times for ⩾**{people}** players for ⩾**{float(duration)}**h..."
                    )
                ).id
            )

            if (
                people == "66"
            ):  # todo re-enable memes - seems the update broke gif embed
                embed = Embed()
                embed.set_image(url=SIXTY_SIX)
                keep_msgs.append((await ctx.send(embed=embed)).id)

            whens = await self.generate_whens_for_channel(event_id, float(duration))

            when = None
            for check_when in whens:
                if check_when[0] == int(people):
                    when = check_when
                    break

            await self.send_when(ctx.channel, when, float(duration), keep_msgs)

    async def send_when(self, channel, when, duration, keep_msgs=None):

        if when:
            embed = Embed(
                title="Availability",
                description=f"for **{when[0]}** players for ⩾**{duration}**h",
                color=0x00FF00,
            )

            for player_ids, times in when[1].items():
                embed.add_field(
                    name=", ".join(
                        sorted([self.players[player_id] for player_id in player_ids])
                    ),
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
        event
            Optional: the name of the event channel to list for
            Default: current channel

        Examples
        --------
          - $list
          - $list dnd
        """
        event_dc_id = await self.get_event_dc_id(ctx, event)
        players = await self.db.get_players(
            await self.event_dc_id_to_event_id(event_dc_id)
        )

        for player in players.keys():
            for chunk in chunks(players[player], 10):
                msg = [f"possible times:\n\n"]
                msg.append(f"_{player}_ at:\n")
                msg.extend(format_timeranges(chunk))
                msg.append("\n")
                await ctx.send("".join(msg))

    @commands.command()
    async def login(self, ctx):
        """Get a magic link to the web interface via DM."""
        warning = (
            "⚠️ this is a magic link which logs in to your account, **don't share it**!"
        )
        link = f"<https://hermes.rdkr.uk/login?token={await self.db.get_magic_token(ctx.message.author.id)}>"
        await ctx.message.author.send(f"{warning}\n\n{link}")

    async def get_event_dc_id(self, ctx, event):
        if not event:
            return str(ctx.message.channel.id)
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
                    return str(channel.id)
        raise KeyError

    async def event_dc_id_to_event_id(self, event_dc_id):
        for event in self.events.values():
            if event.event_dc_id == event_dc_id:
                return event.event_id
        return KeyError
