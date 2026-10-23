from collections import Counter
from timeit import timeit


def count_loop(words: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def count_counter(words: list[str]) -> dict[str, int]:
    return dict(Counter(words))


if __name__ == "__main__":
    words = ["python", "api", "python", "testing"] * 10000
    print("Same result:", count_loop(words) == count_counter(words))
    print("Loop:", timeit(lambda: count_loop(words), number=10))
    print("Counter:", timeit(lambda: count_counter(words), number=10))
