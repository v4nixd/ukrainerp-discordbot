from disnake import AppCommandInteraction, Embed, Color
from disnake.ext import commands
from disnake import app_commands

from version import __version__

class Version(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command()
    @commands.guild_only()
    async def version(self, interaction: AppCommandInteraction):
        await interaction.response.send_message(f"📦 Версія боту - `{__version__}`", ephemeral=True)

def setup(client):
    client.add_cog(Version(client))