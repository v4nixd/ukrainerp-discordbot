from disnake import ui, DiscordException

from ui.error_handler.button.report_to_dev import ReportToDevButton
from ui.error_handler.button.detailed_report import DetailedReportButton

class ErrorHandlerView(ui.View):
    def __init__(self, error: DiscordException):
        super().__init__(timeout=None)
        self.add_item(
            ReportToDevButton(error)
        )
        self.add_item(
            DetailedReportButton(error)
        )