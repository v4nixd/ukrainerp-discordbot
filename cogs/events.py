from disnake.ext import commands

from logger import logger
from ui.selfrole.view.server_select_view import ServerSelectView
from constants import ID

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_connect(self) -> None:
        logger.info("Connected to Discord")

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        logger.info("Logged into Discord")

        self.client.add_view(ServerSelectView(self.client.get_guild(ID.GUILD)))

    @commands.Cog.listener()
    async def on_resumed(self) -> None:
        logger.warning("Resumed session")

    @commands.Cog.listener()
    async def on_disconnect(self) -> None:
        logger.error("Disconnected from Discord")

def setup(client):
    client.add_cog(Events(client))