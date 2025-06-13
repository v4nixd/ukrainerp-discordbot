import traceback

from disnake import ui, ButtonStyle, Interaction, DiscordException, Embed

from ui.error_handler.view.report_to_dev_view import ReportToDevView

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
            embed=Embed(
                title="📄 Детальний звіт помилки",
                color=0xff0000
            )
            .add_field(
                name=f"⚠️ - {str(self.error).split(":")[0]}",
                value=f"```\n{str(traceback.format_exception(self.error))[-1000:]}\n```"
            )
            .set_footer(
                text=f"Натисніть кнопку нижче, якщо бажаєте повідомити розробнику про цю помилку."
            ),
            view=ReportToDevView(self.error),
            ephemeral=True
        )

#TODO - IMPLEMENT report_to_dev_view