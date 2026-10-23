def main() -> None:
    print("For loop:")
    for number in range(1, 6):
        print(number)

    print("While loop:")
    countdown = 3
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Go!")


if __name__ == "__main__":
    main()
