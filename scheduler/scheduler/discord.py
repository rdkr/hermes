from collections import defaultdict
from datetime import datetime, timedelta
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


class Scheduler(commands.Cog):
    """A discord.py Cog to collect and interpret times that users are free to help schedule an event"""

    def __init__(self, bot):
        self.bot = bot
        self.db = PlayerDB()

        self.clean.start()

    @commands.Cog.listener()
    async def on_error(self, event):
        print(event)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        print_exception(type(exception), exception, exception.__traceback__)
        await ctx.send(f"error!")

    @tasks.loop(minutes=1)
    async def clean(self):
        self.db.clean_times()

    @commands.command()
    async def free(self, ctx, *, when):
        """Add a time range for which you are free.

        This command must be performed in the event channel you are
        marking yourself free for.

        You must have set a default timezone before using this command.
        See "$help tz" for more information about how to do this.

        Parameters
        ----------
        when
            Text describing a range within the next fortnight in which
            you are free, generally of the form:

            "<day or date> <time range>"

            <day or date> can be relative, e.g. "tuesday" or "next
            wednesday", or absolute in the US format (month first)

            <time range> should specify two times separated by "-" and
            can use 24h clock (requires colons), AM/PM, or words like
            "morning", "evening". Note that midnight is at the start of
            the day, so "morning-midnight" is not valid for example.

        Examples
        --------
          - $free tomorrow 10am-12pm
          - $free next wednesday 1-2pm
          - $free friday 13:00-17:00
          - $free 12/19 13:00-17:00
        """
        try:
            tz = timezone(self.db.get_tz(ctx.message.author.name))
            timerange = await self.method_name(tz, when)
        except KeyError:
            return await ctx.send(
                f"error: set a tz first using `$tz`. see `$help tz` for more information"
            )
        except AssertionError:
            return await ctx.send(
                f"error: could not parse (see `$help free` for tips)"
            )

        event_id = await self.get_event_id(ctx, None)
        self.db.add_time(ctx.message.author.name, timerange, event_id)
        return await ctx.send(f"added: {format_range(timerange)}")

    async def method_name(self, tz, when):
        result = timefhuman(when)
        if not result:
            raise Exception(f"no times found ({when})")
        if (
                not isinstance(result, tuple)
                or len(result) != 2
                or result[0] >= result[1]
        ):
            raise Exception(f"can't make range ({result})")

        start, end = tz.localize(result[0]), tz.localize(result[1])
        timerange = DateTimeRange(start, end)
        week = DateTimeRange(datetime.now(tz), datetime.now(tz) + timedelta(days=7))
        if timerange not in week:
            raise Exception(f"range outside of next 7 days ({timerange})")
        return timerange

    @commands.command()
    async def when(self, ctx, people=5, duration=1.5, event=None):
        """Find times for an event.

        This will return timeranges in which at least <people> number of
        players are free for at least <duration> length for the given
        event channel.

        Parameters
        ----------
        people
            Optional: the number of people who need to be available
            Default: 5
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
          - $when 3 2
          - $when 3 2 dnd
        """
        event_id = await self.get_event_id(ctx, event)

        if people == 66:
            await ctx.send(SIXTY_SIX)

        # todo fix this mess
        result = defaultdict(list)
        for player, timeranges in self.db.get_players(event_id).items():
            for timerange in timeranges:
                result[player].append(timerange.datetimerange())

        result = find_times(result, people)
        result = filter_times(result, duration)
        result = deduplicate_times(result)

        msg = [f"possible times for ⩾**{people}** players for ⩾**{duration}**h:\n\n"]
        for players, times in result.items():
            msg.append(f"_{', '.join(players)}_ at:\n")
            msg.extend(format_datetimeranges(times))
            msg.append("\n")

        return await ctx.send("".join(msg))

    @commands.command()
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

        msg = [f"possible times:\n\n"]
        for player in who:
            msg.append(f"_{player}_ at:\n")
            msg.extend(format_timeranges(players[player]))
            msg.append("\n")

        await ctx.send("".join(msg))

    @commands.command()
    async def delete(self, ctx, which):
        """Delete timeranges for which you are marked as free.

        Use "$list" first to find the id numbers for timeranges.

        Parameters
        ----------
        which
            The timerange id to delete, or "all"

        Examples
        --------
          - $delete 66
          - $delete all
        """
        if which == "all":
            self.db.delete_times(ctx.message.author.name)
            await ctx.send(f"$deleting: all")
        else:
            self.db.delete_time(ctx.message.author.name, int(which))
            await ctx.send(f"$deleting: {int(which)}")

    @commands.command()
    async def tz(self, ctx, tz):
        """Set your default timezone.

        This must be set in order to add times you are free.

        Parameters
        ----------
        tz
            Your timezone in tz format.

        Examples
        --------
            - $tz Europe/London
        """
        self.db.set_tz(ctx.message.author.name, timezone(tz).zone)
        await ctx.send(f"set: {tz}")


    async def get_event_id(self, ctx, event):
        if not event:
            return ctx.message.channel.id
        else:
            for channel in self.bot.get_all_channels():
                if isinstance(channel, TextChannel) and channel.name == event and ctx.message.author in channel.members:
                    await ctx.send(f"assuming channel: {channel.guild.name}/{channel.name} ({channel.id})")
                    return channel.id
        raise KeyError
