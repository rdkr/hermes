import logging
import os

from discord.ext import commands

from scheduler import Scheduler


def main():
    logging.basicConfig(level=logging.INFO)
    bot = commands.Bot(command_prefix="$")
    bot.add_cog(Scheduler(bot))
    bot.run(os.environ["DISCORD_TOKEN"])


if __name__ == "__main__":
    main()
