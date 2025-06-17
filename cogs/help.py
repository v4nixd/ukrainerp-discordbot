from disnake import AppCommandInteraction, Embed, Color
from disnake.ext import commands
from disnake import app_commands

from logger import logger
from constants import ID, HELP_FOOTER_IMG

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(description="Допомога з використанням бота")
    @commands.guild_only()
    async def help(self, interaction: AppCommandInteraction):
        logger.info(f"[HELP] user with name `{interaction.user.name}` used `/help` command")

        help_embed = Embed(
            title="🛠 Допомога",
            color=Color.blurple()
        )

        commands_text = ""

        for command in self.client.get_guild_slash_commands(ID.GUILD):
            name = f"/{command.name}"
            description = command.description or "Немає опису"
            commands_text += f"`{name}` - {description}\n"

        help_embed.add_field(
            name=f"Ось список доступних команд:",
            value=commands_text,
            inline=False
        )

        help_embed.set_footer(text="UkraineRP Bot • powered by v4nixd", icon_url=HELP_FOOTER_IMG)

        await interaction.send(embed=help_embed, ephemeral=True)

def setup(client):
    client.add_cog(Help(client))