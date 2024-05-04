import logging
from enum import Enum


class LogFormatter(logging.Formatter):
    """Custom formatter for logging messages."""

    grey = "\x1b[38;21m"
    blue = "\x1b[34;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    format = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    )

    FORMATS = {
        logging.DEBUG: blue + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        """Format log record."""
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class LogLevel(Enum):
    """Log levels."""

    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


class LogConfig:
    """Logging configuration."""

    def __init__(self, level: LogLevel = LogLevel.INFO):
        """Initialize logging configuration.

        Args:
            level (LogLevel, optional): Log level. Defaults to LogLevel.INFO.
        """
        self.level = level
        self.logger = logging.getLogger()
        self.logger.setLevel(self.level.value)
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(LogFormatter())
        self.logger.addHandler(self.handler)
        self.logger.propagate = False

    def set_level(self, level: LogLevel):
        """Set log level.

        Args:
            level (LogLevel): Log level.
        """
        self.level = level
        self.logger.setLevel(self.level.value)

    def get_level(self) -> LogLevel:
        """Get log level.

        Returns:
            LogLevel: Log level.
        """
        return self.level


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

if len(logger.handlers) == 0:
    log_config = LogConfig()
    logger.addHandler(log_config.handler)
    logger.propagate = False
    logger.debug("logger initialized")
