from disnake import ui, ButtonStyle, Interaction, DiscordException

from bot import client
from constants import ID

from ui.error_handler.embed import report_to_dev_embed

class ReportToDevButton(ui.Button):
    def __init__(self, error: DiscordException):
        self.error = error
        super().__init__(
            label="Поскаржитися на баг",
            style=ButtonStyle.red,
            emoji="🔍"
        )

    async def callback(self, interaction: Interaction):
        try:
            await client.get_user(ID.DEV_ID).send(content=f"`user mention` - {interaction.user.mention}\n`username` - {interaction.user.name}\n`userid` - {interaction.user.id}\n`channel mention` - {interaction.channel.mention}\n`channelid` - {interaction.channel.id}", embed=report_to_dev_embed.get(self.error))
            await interaction.response.send_message(embed=report_to_dev_embed.get(self.error), ephemeral=True)
        except Exception:
            await interaction.response.send_message(f"⚠️ - Виникла непередбачена помилка. Наразі неможливо надіслати звіт автоматично. Ви можете звернутися до <@{ID.DEV_ID}>.")

#TODO - Polish and implement sending reports to my DM's