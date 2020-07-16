import logging
import os

from discord.ext import commands

from scheduler.discord import Scheduler


def main():
    logging.basicConfig(level=logging.INFO)
    bot = commands.Bot(command_prefix=os.environ.get("HERMES_PREFIX", "$"))
    bot.add_cog(Scheduler(bot))
    bot.run(os.environ["DISCORD_TOKEN"])

if __name__ == "__main__":
    main()
