import os
import logging
from loguru import logger

DEFAULT_FORMAT = os.environ.get("LOGGING_DEFAULT_FORMAT", "<green>[{time}]</green><level>[{level}]</level>: {message}")
DEFAULT_LEVEL = os.environ.get("LOGGING_DEFAULT_LEVEL", "DEBUG")


def create_message_filter(name):
    def message_filter(record):
        return record["extra"].get("name") == name

    return message_filter


logging.disable(logging.WARNING)
logger.remove()


class Logger:
    def __init__(self, name, format=DEFAULT_FORMAT, level=DEFAULT_LEVEL, output=os.sys.stderr, **kwargs):
        self.name = name
        logger.add(output, format=format, level=level, filter=create_message_filter(name), **kwargs)
        self._logger = logger.bind(name=name).opt(colors=True)

    def trace(self, message, *args, **kwargs):
        return self._logger.trace(message, *args, **kwargs)

    def debug(self, message, *args, **kwargs):
        return self._logger.debug(message, *args, **kwargs)

    def info(self, message, *args, **kwargs):
        return self._logger.info(message, *args, **kwargs)

    def success(self, message, *args, **kwargs):
        return self._logger.success(message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        return self._logger.warning(message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        return self._logger.error(message, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        return self._logger.error(message, *args, **kwargs)
