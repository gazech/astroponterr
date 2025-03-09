import logging
from typing import ClassVar, Dict


class ColorFormatter(logging.Formatter):
    """Custom formatter that applies different formats based on log level"""

    # ANSI color codes
    COLORS: ClassVar[Dict[int, str]] = {
        logging.DEBUG:    "\033[2m", # de-emphasized
        logging.INFO:     "\033[0m", # Normal
        logging.WARNING:  "\033[7m", # Inverted
        logging.ERROR:    "\033[91m", # Red
        logging.CRITICAL: "\033[91;7m", # Red, inverted
    }

    RESET: ClassVar[str] = "\033[0m"

    def __init__(self) -> None:
        """Initialize the formatter with level-specific formats"""
        super().__init__()
        self.formatting_strings: Dict[int, str] = {
            lvl: f"{self.COLORS[lvl]}%(asctime)s : \033[1m%(levelname)8s\033[0m{self.COLORS[lvl]} | %(module)s:%(funcName)s:%(lineno)d > %(message)s{self.RESET}" for lvl in self.COLORS
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


class Scribe(logging.Logger):
    """Custom logger with level-specific formatting"""

    def __init__(self, name: str, level: int = logging.DEBUG) -> None:
        super().__init__(name, level)
        self.setup_handler()

    def setup_handler(self) -> None:
        handler = logging.StreamHandler()
        handler.setFormatter(ColorFormatter())
        self.addHandler(handler)

    def test_levels(self) -> None:
        for level in (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL):
            self.log(level, f"This is a test message at level {level} with value {logging.getLevelName(level)}")

def main():
    logger = Scribe("my_logger", logging.DEBUG)
    logger.test_levels()  # Logs a test message to the console

if __name__ == "__main__":
    main()

