def divide(first: float, second: float) -> float:
    if second == 0:
        raise ValueError("The divisor must not be zero.")
    return first / second


def main() -> None:
    try:
        print(divide(10, 2))
        print(divide(10, 0))
    except ValueError as error:
        print("Could not calculate:", error)


if __name__ == "__main__":
    main()
