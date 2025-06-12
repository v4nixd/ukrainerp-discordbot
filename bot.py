import disnake

from disnake.ext import commands

client = commands.Bot(
    command_prefix=".",
    test_guilds=[1336148824007249942],
    intents=disnake.Intents.all()
)