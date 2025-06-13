import disnake

from disnake.ext import commands

from constants import ID

client = commands.Bot(
    command_prefix=".",
    test_guilds=[ID.GUILD],
    intents=disnake.Intents.all(),
    reload=True
)