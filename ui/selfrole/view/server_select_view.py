from disnake import ui, ButtonStyle, PartialEmoji, Guild

from ui.selfrole.button.server_select_button import ServerSelectButton
from utils import getRole
from constants import ID

class ServerSelectView(ui.View):
    def __init__(self, guild: Guild):
        super().__init__(timeout=None)
        self.add_item(
            ServerSelectButton(
                label="UkraineRP #1",
                style=ButtonStyle.gray,
                disabled=False,
                custom_id="uarp1_selfrole_button",
                emoji=PartialEmoji.from_str(f"uarp1:{ID.Emoji.UARP_1}"),
                role=getRole(guild, ID.Role.UKRAINERP_1)
            )
        )
        self.add_item(
            ServerSelectButton(
                label="UkraineRP #2",
                style=ButtonStyle.gray,
                disabled=False,
                custom_id="uarp2_selfrole_button",
                emoji=PartialEmoji.from_str(f"uarp2:{ID.Emoji.UARP_2}"),
                role=getRole(guild, ID.Role.UKRAINERP_2)
            )
        )