def linear_search(items: list[int], target: int) -> int | None:
    for index, value in enumerate(items):
        if value == target:
            return index
    return None


def binary_search(sorted_items: list[int], target: int) -> int | None:
    left, right = 0, len(sorted_items) - 1
    while left <= right:
        middle = (left + right) // 2
        if sorted_items[middle] == target:
            return middle
        if sorted_items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return None


def main() -> None:
    values = [3, 7, 12, 18, 24, 31]
    print("Linear:", linear_search(values, 18))
    print("Binary:", binary_search(values, 18))


if __name__ == "__main__":
    main()
