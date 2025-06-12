import logging
import sys

from colorama import init, Fore, Style

class ColoredFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN + Style.BRIGHT,
        logging.WARNING: Fore.YELLOW + Style.BRIGHT,
        logging.ERROR: Fore.RED + Style.BRIGHT,
        logging.CRITICAL: Fore.RED + Style.BRIGHT + Style.BRIGHT
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelno, "")
        formatted_msg = super().format(record)
        return f"{log_color}{formatted_msg}{Style.RESET_ALL}"
    
def setup_logger(name: str, log_file: str = "ukrainerpbot.log") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    format_str = "%(asctime)s | %(levelname)-8s | %(message)s"
    file_formatter = logging.Formatter(format_str)
    color_formatter = ColoredFormatter(format_str)

    file_handler = logging.FileHandler(log_file, encoding="utf-8", mode="a")
    file_handler.setFormatter(file_formatter)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(color_formatter)

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

logger: logging.Logger = setup_logger("ukrainerpbot")