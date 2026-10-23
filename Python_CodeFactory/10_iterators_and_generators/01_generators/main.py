def even_numbers(limit: int):
    number = 0
    while number <= limit:
        yield number
        number += 2


def main() -> None:
    for value in even_numbers(10):
        print(value)


if __name__ == "__main__":
    main()
