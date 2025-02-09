## 2. **`utils/logger.py`** (Logger Setup)

from rich.logging import RichHandler
import logging

def setup_logging(console):
    # Configure Rich logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(console=console)]
    )
    logging.info("Logging initialized with Rich.")
