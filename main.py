import os

from dotenv import load_dotenv

from bot import client
from logger import logger
from version import __version__

import sentry_sdk

if __name__=="__main__":
    sentry_sdk.init(
        dsn=os.getenv("SENTRY_DSN"),
        send_default_pii=True,
        traces_sample_rate=1.0,
        _experiments={
            "enable_logs": True,
        },
        release=f"uarpbot@{__version__}"
    )

    logger.debug("HOUSTON WE GOT NO PROBLEMS")
    load_dotenv()
    client.load_extensions("cogs")
    client.run(token=os.getenv("BOT_TOKEN"))