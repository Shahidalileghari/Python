def main() -> None:
    first, second = 17, 5
    print("Addition:", first + second)
    print("Division:", first / second)
    print("Floor division:", first // second)
    print("Remainder:", first % second)
    print("Power:", first ** second)
    print("Is first larger?", first > second)
    print("Both positive?", first > 0 and second > 0)


if __name__ == "__main__":
    main()
