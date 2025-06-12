import os

from dotenv import load_dotenv

from bot import client
from logger import logger

if __name__=="__main__":
    logger.debug("HOUSTON WE GOT NO PROBLEMS")
    load_dotenv()
    client.load_extensions("cogs")
    client.run(token=os.getenv("BOT_TOKEN"))