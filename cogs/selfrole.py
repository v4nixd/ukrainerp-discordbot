from disnake import AppCommandInteraction, Embed, DiscordException, Color
from disnake.ext import commands

from ui.selfrole.view.server_select_view import ServerSelectView
from ui.error_handler.view.error_handler_view import ErrorHandlerView
from logger import logger
from constants import ID

class SelfRole(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.slash_command(description="Ініціалізація меню вибору сервера")
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def init_selfrole(self, interaction: AppCommandInteraction) -> None:
        await interaction.channel.send(embed=Embed(title="Оберіть сервер, на якому ви граєте.", color=Color.blurple()), view=ServerSelectView(interaction.guild))
        await interaction.response.send_message("✅", ephemeral=True)
        logger.info(f"[SERVER SELECT] menu initialized by user `{interaction.user.name}`")

    @init_selfrole.error
    async def init_selfrole_error(self, interaction: AppCommandInteraction, error: DiscordException) -> None:
        if isinstance(error, commands.MissingPermissions):
            logger.warning(f"[COMMAND WARN] selfrole - someone tried using init_selfrole without admin permissions!")
            await interaction.response.send_message("❌ У вас немає прав адміністратора.", ephemeral=True)
            return
        try:
            logger.error(f"[COMMAND ERROR] selfrole - init_selfrole failed: {type(error).__name__}: {error}")
            if interaction.response.is_done():
                await interaction.followup.send(
                    content=f"## ❌ Виникла помилка!\n```\n{error}\n```\nПовідомте про це <@{ID.DEV_ID}>",
                    view=ErrorHandlerView(error),
                    ephemeral=True
                )
            else:
                await interaction.response.send_message(
                    content=f"## ❌ Виникла помилка!\n```\n{error}\n```\nПовідомте про це <@{ID.DEV_ID}>",
                    view=ErrorHandlerView(error),
                    ephemeral=True
                )
        except Exception as e:
            logger.exception(f"❌ Error while sending error message\n{e}")

def setup(client):
    client.add_cog(SelfRole(client))