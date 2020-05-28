from collections import defaultdict
from datetime import datetime, timedelta
from traceback import print_exception

from datetimerange import DateTimeRange
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
        """specify a time range when you are free

        e.g. "$free tomorrow 10am-12pm" or "$free friday 5:30-7pm"
        """
        try:
            result = timefhuman(when)
            if not result:
                raise Exception(f"no times found ({when})")
            if (
                not isinstance(result, tuple)
                or len(result) != 2
                or result[0] >= result[1]
            ):
                raise Exception(f"can't make range ({result})")
            tz = timezone(self.db.get_tz(ctx.message.author.name))
            start, end = tz.localize(result[0]), tz.localize(result[1])
            timerange = DateTimeRange(start, end)
            week = DateTimeRange(datetime.now(tz), datetime.now(tz) + timedelta(days=7))
            if timerange not in week:
                raise Exception(f"range outside of next 7 days ({timerange})")
        except KeyError:
            return await ctx.send(
                f"error: set a tz first using `$tz`. see `$help tz` for more information"
            )
        except AssertionError:
            return await ctx.send(
                f"error: could not parse (try US style dates and : in 24h times)"
            )

        self.db.add_time(ctx.message.author.name, timerange)
        return await ctx.send(f"added: {format_range(timerange)}")

    @commands.command()
    async def when(self, ctx, people=5, duration=1.5):
        """find times that work for multiple people

        this will timeranges of at least <duration> length in which at
        least <people> number of players are free

        e.g. "$when" "$when 3", or "$when 2 4"
        """
        if people == 66:
            return await ctx.send(SIXTY_SIX)

        # todo fix this mess
        result = defaultdict(list)
        for player, timeranges in self.db.get_players().items():
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
    async def list(self, ctx, who=None):
        """list when you or others are marked as free

        e.g. "$list" "$list Jon", or "$list all"
        """
        players = self.db.get_players()

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
    async def delete(self, ctx, which, who=None):
        """delete when you or others are marked as free

        e.g. "$delete 1", "$delete all", "$delete 1 Jon"
        """
        if not who:
            who = ctx.message.author.name
        if which == "all":
            self.db.delete_times(who)
            await ctx.send(f"$deleting: all")
        else:
            self.db.delete_time(who, int(which))
            await ctx.send(f"$deleting: {int(which)}")

    @commands.command()
    async def tz(self, ctx, tz):
        """set your timezone

        e.g. "$tz Europe/London"
        """
        self.db.set_tz(ctx.message.author.name, timezone(tz).zone)
        await ctx.send(f"set: {tz}")
