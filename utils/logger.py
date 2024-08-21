import logging
import os
from datetime import datetime

LOGGING_LEVEL = os.environ.get("LOGLEVEL", "INFO").upper()
LOGGING_DIR = "logs"


def start_logging():
    """
    A wrapper function to set up basic logging configuration.

    Parameters
    ----------
    levels: :obj:`str`
        logging level options:
        'CRITICAL'
        'ERROR'
        'WARNING'
        'INFO'
        'DEBUG'
    """
    current_date = datetime.now().strftime("%Y%m%d")
    filename = f"{LOGGING_DIR}/blessuk_log_{current_date}"

    os.makedirs(LOGGING_DIR, exist_ok=True)

    # Create a logger for blessuk
    logger = logging.getLogger("blessuk")
    logger.setLevel(LOGGING_LEVEL)

    # Ensure we don't duplicate handlers
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s"
        )

        file_handler = logging.FileHandler(f"{filename}.log")
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger
