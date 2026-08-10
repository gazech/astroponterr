import logging
from typing import ClassVar, Dict


class FormatterBaseClass(logging.Formatter):
    pass


class BasicFormatter(logging.Formatter):
    pass


class ColorFormatter(logging.Formatter):
    """Custom formatter that applies different formats based on log level"""

    # ANSI color codes
    COLORS: ClassVar[Dict[int, str]] = {
        logging.DEBUG: "\033[2m",  # de-emphasized
        logging.INFO: "\033[0m",  # Normal
        logging.WARNING: "\033[7m",  # Inverted
        logging.ERROR: "\033[91m",  # Red
        logging.CRITICAL: "\033[91;7m",  # Red, inverted
    }

    RESET: ClassVar[str] = "\033[0m"

    def __init__(self) -> None:
        """Initialize the formatter with level-specific formats"""
        super().__init__()
        self.formatting_strings: Dict[int, str] = {
            lvl: f"{self.COLORS[lvl]}%(asctime)s : \033[1m%(levelname)8s\033[0m{self.COLORS[lvl]} | %(name)s:%(funcName)s:%(lineno)d > %(message)s{self.RESET}"
            for lvl in self.COLORS
        }
        self.formatters: Dict[int, logging.Formatter] = {
            lvl: logging.Formatter(f"{self.formatting_strings[lvl]}") for lvl in self.COLORS
        }

    def format(self, record: logging.LogRecord) -> str:
        """Apply the appropriate format based on the log level"""
        formatter = self.formatters.get(record.levelno)
        if formatter is None:
            formatter = self.formatters[logging.DEBUG]
        return formatter.format(record)
