import logging

from astroponterr.logging.format import ColorFormatter


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

