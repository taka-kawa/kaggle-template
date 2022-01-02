# Standard Library
import functools
import time
from contextlib import contextmanager
from typing import Callable


class TimeUtil:
    @staticmethod
    @contextmanager
    def timer(name: str):
        start_time = time.time()
        yield
        end_time = time.time()
        print(f"[{name}] done in {end_time - start_time:.4f} s")

    @staticmethod
    def timer_wrapper(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            print(f"[{func.__name__}] start")
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"[{func.__name__}] done in {end_time - start_time:.4f} s")

            return result

        return wrapper
