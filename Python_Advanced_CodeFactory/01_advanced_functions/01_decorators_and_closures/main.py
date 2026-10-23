from functools import wraps
from time import perf_counter
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def announce(prefix: str) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorate(function: Callable[P, R]) -> Callable[P, R]:
        @wraps(function)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            print(f"{prefix}: {function.__name__}")
            return function(*args, **kwargs)
        return wrapper
    return decorate


def measure_time(function: Callable[P, R]) -> Callable[P, R]:
    @wraps(function)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        started = perf_counter()
        try:
            return function(*args, **kwargs)
        finally:
            print(f"Elapsed: {perf_counter() - started:.6f}s")
    return wrapper


@announce("TRACE")
@measure_time
def calculate_total(values: list[float]) -> float:
    return sum(values)


if __name__ == "__main__":
    print(calculate_total([12.5, 3.0, 9.5]))
