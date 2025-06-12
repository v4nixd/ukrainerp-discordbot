import os

from dotenv import load_dotenv

from bot import client
from logger import logger
from ui.selfrole.view.server_select_view import ServerSelectView

@client.event
async def on_connect():
    logger.info("Connected to Discord")

@client.event
async def on_ready():
    logger.info("Logged into Discord")

    client.add_view(ServerSelectView(client.get_guild(1336148824007249942)))

if __name__=="__main__":
    logger.debug("HOUSTON WE GOT NO PROBLEMS")
    load_dotenv()
    client.load_extensions("cogs")
    client.run(token=os.getenv("BOT_TOKEN"))