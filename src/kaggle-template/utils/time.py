# Standard Library
import functools
import time
from contextlib import contextmanager
from typing import Callable

from .logger import get_logger

logger = get_logger(__name__)

@contextmanager
def timer(name: str):
    start_time = time.time()
    yield
    end_time = time.time()
    logger.info(f"[{name}] done in {end_time - start_time:.4f} s")


def timer_wrapper(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info(f"[{func.__name__}] start")
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"[{func.__name__}] done in {end_time - start_time:.4f} s")

        return result

    return wrapper
