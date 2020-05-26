from collections import defaultdict
from datetime import datetime, timedelta
from traceback import print_exc

from datetimerange import DateTimeRange
from discord.ext import commands, tasks
from pytz import timezone
from timefhuman import timefhuman

from scheduler.dynamodb import PlayerDB
from scheduler.scheduler import filter_times, find_times

SIXTY_SIX = "https://pa1.narvii.com/7235/5ceb289c2b7953a679dafaf9fc7f4f6ab0afc394r1-480-208_hq.gif"


class Scheduler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel = None
        self.errors = 0
        self.db = PlayerDB()

        self.clean.start()

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
                f"`error: set a tz first using `$tz`. see `$help tz` for more information"
            )
        except AssertionError:
            return await ctx.send(
                f"`error: could not parse (try US style dates and : in 24h times)`"
            )
        except Exception as exc:
            print(f"error: {exc} ({when}):")
            print_exc()
            return await ctx.send(f"error: `{exc}`")

        self.db.add_time(ctx.message.author.name, timerange)
        return await ctx.send(f"added: {format_range(timerange)}")

    @commands.command()
    async def when(self, ctx, people=4, duration=1.5):
        """find times that work for multiple people

        this will timeranges of at least <duration> length in which at
        least <people> number of players are free

        e.g. "$when" "$when 3", or "$when 2 4"
        """
        if people == 66:
            return await ctx.send(SIXTY_SIX)

        result = filter_times(find_times(self.db.get_players(), people), duration)

        sorted_result = defaultdict(list)
        for players in sorted(result, key=len, reverse=True):
            for times in result[players]:
                skip = False
                for already_people, already_times in sorted_result.items():
                    for already_time in already_times:
                        if times in already_time and players.issubset(already_people):
                            skip = True
                if not skip:
                    sorted_result[players].append(times)

        msg = [f"possible times for ⩾**{people}** players for ⩾**{duration}**h:\n\n"]
        for players, times in sorted_result.items():
            msg.append(f"_{', '.join(players)}_ at:\n")
            msg.extend(format_ranges(times))
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
            msg.extend(format_ranges(players[player]))
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
            await ctx.send(f"removed: all")
        else:
            self.db.delete_time(who, int(which) - 1)
            await ctx.send(f"removed: {which}")

    @commands.command()
    async def tz(self, ctx, timezone):
        """set your timezone

        e.g. "$tz Europe/London"
        """
        self.db.set_tz(ctx.message.author.name, timezone(timezone).zone)
        await ctx.send(f"set: {timezone}")

    @tasks.loop(minutes=1)
    async def clean(self):
        now = datetime.now(timezone("Europe/London"))
        for player, timeranges in self.db.get_players().items():
            for i, timerange in enumerate(timeranges):
                if timerange.end_datetime < now:
                    print(f"removing: {player}, {timerange}, {i}")
                    self.db.delete_time(player, i)
                    break  # we can only clear one per run as the index will change

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        await ctx.send(f"error: `{exception}`")


def format_ranges(ranges):
    msg = list()

    if not ranges:
        msg.append("• none\n")
        return msg

    for i, timerange in enumerate(ranges):
        msg.append(f" • `{i+1:02}` {format_range(timerange)} \n")

    return msg


def format_range(timerange):

    timerange.start_time_format = "%a"
    day = timerange.get_start_time_str()

    timerange.start_time_format = "%d"
    date = timerange.get_start_time_str()
    date_suffix = (
        "th"
        if 11 <= int(date) <= 13
        else {1: "st", 2: "nd", 3: "rd"}.get(int(date) % 10, "th")
    )

    timerange.start_time_format = "%H:%M"
    timerange.end_time_format = "%H:%M (%Z)"
    time_start = timerange.get_start_time_str()
    time_end = timerange.get_end_time_str()

    return f"{day} {date}{date_suffix} @ {time_start} - {time_end}"
