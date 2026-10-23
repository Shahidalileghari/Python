def main() -> None:
    name = input("What is your name? ").strip()
    age_text = input("How old are you? ").strip()

    if not age_text.isdigit():
        print("Please enter age as a whole number.")
        return

    age = int(age_text)
    print(f"Hello, {name or 'student'}! Next year you will be {age + 1}.")


if __name__ == "__main__":
    main()
