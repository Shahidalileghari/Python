from functools import lru_cache


@lru_cache(maxsize=256)
def fibonacci(number: int) -> int:
    if number < 0:
        raise ValueError("number must be non-negative")
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


if __name__ == "__main__":
    print("Fibonacci(35):", fibonacci(35))
    print("Cache stats:", fibonacci.cache_info())
