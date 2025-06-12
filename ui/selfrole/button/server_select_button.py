from disnake import ui, ButtonStyle, Emoji, PartialEmoji, Interaction, Role

from logger import logger

class ServerSelectButton(ui.Button):
    def __init__(self, label: str, style: ButtonStyle, disabled: bool, custom_id: str, emoji: str | Emoji | PartialEmoji, role: Role):
        self.role = role
        super().__init__(
            label=label,
            style=style,
            disabled=disabled,
            custom_id=custom_id,
            emoji=emoji
        )

    async def callback(self, interaction: Interaction):
        if self.role in interaction.user.roles:
            await interaction.user.remove_roles(self.role)
            await interaction.send(f"❌ Вам видалена роль {self.role.mention}", ephemeral=True)
            logger.info(f"[SERVER SELECT] role `{self.role.name}` with id `{self.role.id}` removed for user with name `{interaction.user.name}` (id - `{interaction.user.id}`)")
        else:
            await interaction.user.add_roles(self.role)
            await interaction.send(f"✅ Вам видана роль {self.role.mention}", ephemeral=True)
            logger.info(f"[SERVER SELECT] role `{self.role.name}` with id `{self.role.id}` added for user with name `{interaction.user.name}` (id - `{interaction.user.id}`)")