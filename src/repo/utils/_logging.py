import inspect
import logging
import os
import sys

import rich.traceback
from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        # Get corresponding Loguru level if it exists.
        level: str | int
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message.
        frame, depth = inspect.currentframe(), 0
        while frame and (depth == 0 or frame.f_code.co_filename == logging.__file__):
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def init_logging(level: int | str = logging.NOTSET) -> None:
    rich.traceback.install(show_locals=True)
    if isinstance(level, int):
        level = logging.getLevelName(level)
    if level in ("NOTSET", logging.NOTSET):
        level = "DEBUG" if os.getenv("RUNNER_DEBUG") in ("1", "true") else "INFO"
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
    logger.remove()
    logger.add(sys.stderr, level=level)
