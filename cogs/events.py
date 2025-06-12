from disnake.ext import commands

from logger import logger
from ui.selfrole.view.server_select_view import ServerSelectView

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_connect(self):
        logger.info("Connected to Discord")

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info("Logged into Discord")

        self.client.add_view(ServerSelectView(self.client.get_guild(1336148824007249942)))

    @commands.Cog.listener()
    async def on_resume(self):
        logger.warning("Resumed session")

    @commands.Cog.listener()
    async def on_disconnect(self):
        logger.error("Disconnected from Discord")

def setup(client):
    client.add_cog(Events(client))