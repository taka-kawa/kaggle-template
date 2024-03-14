# Standard Library
import logging
import sys

# Third Party
from tqdm import tqdm


class TqdmLoggingHandler(logging.Handler):
    colors = {"INFO": "\033[37m{}\033[0m"}

    def __init__(self, level=logging.NOTSET):
        super().__init__(level)

    def emit(self, record):
        try:
            record.msg = TqdmLoggingHandler.colors.get(record.levelname, "{}").format(
                record.msg
            )
            msg = self.format(record)
            tqdm.write(msg, file=sys.stderr)
            self.flush()
        except Exception:
            self.handleError(record)


class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    green = "\x1b[32;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "[%(asctime)s] [%(levelname)s] [%(process)d] [%(name)s] [%(funcName)s] [%(lineno)d] %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_logger(name: str, level: int = logging.DEBUG) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Clear existing handler
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.propagate = False

    # create console handler with a INFO log level
    ch = TqdmLoggingHandler()
    ch.setFormatter(CustomFormatter())

    # add the handlers to the logger
    logger.addHandler(ch)

    return logger