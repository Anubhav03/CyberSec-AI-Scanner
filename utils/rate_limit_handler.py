import time
import random
from typing import Callable
from utils.logger import get_logger

log = get_logger("RateLimiter")


def with_backoff(retries: int = 5, base_delay: float = 1.5):
    """Retry decorator with exponential backoff for API calls."""
    def wrapper(func: Callable):
        def inner(*args, **kwargs):
            delay = base_delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    log.warning(f"⚠ API Rate Limit Hit: {e}")
                    log.info(f"Retrying in {delay:.2f}s...")
                    time.sleep(delay + random.uniform(0, 0.5))
                    delay *= 2
            raise RuntimeError("❌ Max retry attempts exceeded.")
        return inner
    return wrapper
