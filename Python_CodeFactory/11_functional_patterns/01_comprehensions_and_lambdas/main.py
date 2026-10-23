def main() -> None:
    numbers = range(1, 11)
    squares = [number * number for number in numbers]
    even_squares = [value for value in squares if value % 2 == 0]
    print("Squares:", squares)
    print("Even squares:", even_squares)

    students = [("Ali", 81), ("Sara", 94), ("Zara", 88)]
    print("Sorted by score:", sorted(students, key=lambda item: item[1]))


if __name__ == "__main__":
    main()
