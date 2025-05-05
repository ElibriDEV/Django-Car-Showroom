import logging
import time
import typing as t
import os
import inspect

from functools import wraps
from pathlib import Path

from core import settings


class _ColoredFormatter(logging.Formatter):
    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class LoggerManager:
    _logger: logging.Logger
    _fmt: logging.Formatter
    _excluded_loggers: t.Sequence[str]

    _stream_enabled: bool = False
    _elastic_enabled: bool = False

    def __init__(
            self,
            fmt: str | None = None,
            min_level: int = 20,
            name: str = None,
            exclude_loggers: t.Sequence[str] = None
    ):
        self._logger = logging.getLogger(name)
        self._fmt = _ColoredFormatter(fmt)
        self._logger.setLevel(min_level)
        if not exclude_loggers:
            self._excluded_loggers = []
        self._excluded_loggers = exclude_loggers
        if self._excluded_loggers:
            for key in logging.root.manager.loggerDict.keys():
                if key.startswith(tuple(exclude_loggers)):
                    logging.getLogger(key).disabled = True

    def add_console_stream(self, formatter: logging.Formatter | None = None):
        if self._stream_enabled:
            return
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter if formatter else self._fmt)
        self._logger.addHandler(console_handler)
        self._stream_enabled = True

    @property
    def logger(self) -> logging.Logger:
        return self._logger

    @property
    def excluded_loggers(self) -> t.Sequence[str]:
        return self._excluded_loggers

    @property
    def stream_enabled(self) -> bool:
        return self._stream_enabled

    @property
    def elastic_enabled(self) -> bool:
        return self._elastic_enabled


_logger_builder = LoggerManager(
    fmt="%(asctime)s [%(levelname)s] [%(filename)s] [%(funcName)s]: %(message)s",
    min_level=logging.DEBUG if settings.DEBUG else logging.INFO,
    exclude_loggers=[
        "elastic_transport.transport",
        "sentence_transformers",
    ]
)
_logger_builder.add_console_stream()
LOGGER = _logger_builder.logger

def _make_decorator_record(func: t.Callable[[...], ...], level: int, message: str, *args):
    record = LOGGER.makeRecord(
        LOGGER.name,
        level,
        Path(os.path.abspath(inspect.getfile(func))).name,
        0,
        message,
        args,
        None,
    )
    record.funcName = func.__name__
    LOGGER.handle(record)


def logger_decorator(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        _make_decorator_record(func, logging.DEBUG, "Started with args=%s, kwargs=%s", args, kwargs)
        start = time.time()
        try:
            result = await func(*args, **kwargs)
        except Exception as e:
            _make_decorator_record(func, logging.ERROR, "%s. Time: %s", e, time.time() - start)
            raise e
        _make_decorator_record(func, logging.DEBUG, "Finished. Time: %s", time.time() - start)
        return result
    return wrapper
