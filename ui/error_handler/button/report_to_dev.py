import traceback

from disnake import ui, ButtonStyle, Interaction, DiscordException, Embed

from bot import client

# from logger import logger

class ReportToDevButton(ui.Button):
    def __init__(self, error: DiscordException):
        self.error = error
        super().__init__(
            label="Поскаржитися на баг",
            style=ButtonStyle.red,
            emoji="🔍"
        )

    async def callback(self, interaction: Interaction):
        # logger.debug(f"```\n{str(traceback.format_exception(self.error))[-1000:]}\n```")
        error_embed = Embed(
            title="📄 Детальний звіт помилки",
            color=0xff0000
        ).add_field(
            name=f"⚠️ - {str(self.error).split(":")[0]}",
            value=f"```\n{str(traceback.format_exception(self.error)).split("\\n")[-2]}\n```"
        ).set_footer(
            text=f"Детальний звіт про помилку надіслано розробнику. Виправлення буде виконано якнайшвидше."
        )

        try:
            await client.get_user(936343190632558593).send(embed=error_embed)
            await interaction.response.send_message(embed=error_embed, ephemeral=True)
        except Exception as e:
            await interaction.response.send_message("⚠️ - Виникла непередбачена помилка. Наразі неможливо надіслати звіт автоматично. Ви можете звернутися до <@936343190632558593>.")

#TODO - Polish and implement sending reports to my DM's