def calculate_area(width: float, height: float) -> float:
    """Return the area of a rectangle."""
    if width < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative.")
    return width * height


def main() -> None:
    print(calculate_area(4, 6))


if __name__ == "__main__":
    main()
