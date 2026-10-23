import random
import time


class TemporaryServiceError(Exception):
    pass


def demo_service(attempt: int) -> str:
    if attempt < 3:
        raise TemporaryServiceError("Temporary demo failure")
    return "success"


def call_with_retries(max_attempts: int = 4) -> str:
    for attempt in range(1, max_attempts + 1):
        try:
            return demo_service(attempt)
        except TemporaryServiceError:
            if attempt == max_attempts:
                raise
            delay = min(0.05 * (2 ** (attempt - 1)), 0.2)
            time.sleep(delay + random.uniform(0, 0.01))
    raise RuntimeError("Unreachable")


if __name__ == "__main__":
    print(call_with_retries())
