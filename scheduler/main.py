import asyncio
import logging
import os

from discord import Intents
from discord.ext import commands

from scheduler.discord import Scheduler


def main():

    logging.basicConfig(level=logging.INFO)

    intents = Intents.default()
    intents.members = True

    bot = commands.Bot(command_prefix=os.environ.get("HERMES_PREFIX", "$"), intents=intents)
    bot.add_cog(Scheduler(bot))
    bot.run(os.environ["DISCORD_TOKEN"])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.set_debug(False)
    loop.run_until_complete(main())
