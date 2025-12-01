import logging
from pathlib import Path

LOG_DIR = Path("./logs")
LOG_DIR.mkdir(exist_ok=True)

def get_logger(name: str):
    """Returns a configured logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if not logger.handlers:
        fh = logging.FileHandler(LOG_DIR / "cybersec_ai.log")
        sh = logging.StreamHandler()

        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] - %(name)s: %(message)s",
            "%Y-%m-%d %H:%M:%S"
        )

        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(sh)

    return logger


# Example usage
if __name__ == "__main__":
    log = get_logger("test")
    log.info("Logger initialized successfully")
