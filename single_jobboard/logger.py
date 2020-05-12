import logging
from rich.logging import RichHandler
import structlog

from .config.logging import LOGGING_MESSAGE_FORMAT, LOGGING_DATE_FORMAT


logging.basicConfig(
    level="NOTSET",
    format=LOGGING_MESSAGE_FORMAT,
    datefmt=LOGGING_DATE_FORMAT,
    handlers=[RichHandler()],
)

logger = logging.getLogger("single_jobboard")
