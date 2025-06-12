from disnake import ui, ButtonStyle, PartialEmoji, Guild

from ui.selfrole.button.server_select_button import ServerSelectButton
from utils import getRole

class ServerSelectView(ui.View):
    def __init__(self, guild: Guild):
        super().__init__(timeout=None)
        self.add_item(
            ServerSelectButton(
                label="UkraineRP #1",
                style=ButtonStyle.gray,
                disabled=False,
                custom_id="uarp1_selfrole_button",
                emoji=PartialEmoji.from_str("uarp1:1382518356615364739"),
                role=getRole(guild, 1382524647165395106)
            )
        )
        self.add_item(
            ServerSelectButton(
                label="UkraineRP #2",
                style=ButtonStyle.gray,
                disabled=False,
                custom_id="uarp2_selfrole_button",
                emoji=PartialEmoji.from_str("uarp2:1382518371928637440"),
                role=getRole(guild, 1382524692287590490)
            )
        )