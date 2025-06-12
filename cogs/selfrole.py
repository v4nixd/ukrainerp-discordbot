from disnake import AppCommandInteraction, Embed, Colour
from disnake.ext import commands

from ui.selfrole.view.server_select_view import ServerSelectView
from logger import logger

class SelfRole(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.slash_command()
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def init_selfrole(self, interaction: AppCommandInteraction):
        await interaction.channel.send(embed=Embed(title="Оберіть на якому сервері ви граєте", color=0x7289DA), view=ServerSelectView(interaction.guild))
        await interaction.response.send_message("✅", ephemeral=True)
        logger.info(f"[SERVER SELECT] menu initialized by user `{interaction.user.name}`")

def setup(client):
    client.add_cog(SelfRole(client))