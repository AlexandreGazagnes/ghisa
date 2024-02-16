"""
Logger module to log the messages
"""

import logging
import os

LOG_LEVEL = logging.INFO


def get_logger(name):
    """Get the logger."""

    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s [%(pathname)s %(funcName)s %(lineno)d]"
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


logger = get_logger(__name__)
