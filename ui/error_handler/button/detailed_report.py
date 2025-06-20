from disnake import ui, ButtonStyle, Interaction, DiscordException

from ui.error_handler.view.report_to_dev_view import ReportToDevView

from ui.error_handler.embed import detailed_report_embed

class DetailedReportButton(ui.Button):
    def __init__(self, error: DiscordException):
        self.error = error
        super().__init__(
            label="Детальний звіт",
            style=ButtonStyle.gray,
            emoji="📄"
        )

    async def callback(self, interaction: Interaction):
        await interaction.response.send_message(
            embed=detailed_report_embed.get(self.error),
            view=ReportToDevView(self.error),
            ephemeral=True
        )