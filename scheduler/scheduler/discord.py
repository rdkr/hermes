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

        self.sync.start()

    @commands.Cog.listener()
    async def on_error(self, event):
        print(event)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        print_exception(type(exception), exception, exception.__traceback__)
        await ctx.send(f"error!")

    # @tasks.loop(seconds=3)
    # async def sync(self):
    #     valid = []
    #     for guild in self.bot.guilds:
    #         for channel in guild.channels:
    #             can_send = channel.permissions_for(guild.me).send_messages
    #             if isinstance(channel, TextChannel) and can_send:
    #                 for member in channel.members:
    #                     if not member == guild.me:
    #                         valid.append((channel.id, member.id))
    #     self.db.sync_event_players(valid)

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
        self.db.set_tz(ctx.message.author.id, ctx.message.author.name, timezone(tz).zone)
        await ctx.send(f"set: {tz}")

    @commands.command()
    async def link(self, ctx):
        """Get a link to the web interface via DM.
        """
        warning = "⚠️ this is a magic link which logs in to your account, **don't share it**!"
        link = f"<https://neel.rdkr.uk/hermes/index.html?token={self.db.get_magic_token(ctx.message.author.id)}>"
        await ctx.message.author.send(f"{warning}\n\n{link}")

    async def get_event_id(self, ctx, event):
        if not event:
            return ctx.message.channel.id
        else:
            for channel in self.bot.get_all_channels():
                if isinstance(channel, TextChannel) and channel.name == event and ctx.message.author in channel.members:
                    await ctx.send(f"assuming channel: {channel.guild.name}/{channel.name} ({channel.id})")
                    return channel.id
        raise KeyError
