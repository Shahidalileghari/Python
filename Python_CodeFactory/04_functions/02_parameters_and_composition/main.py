def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"


def make_title(text: str) -> str:
    return text.strip().title()


def main() -> None:
    print(greet("Sam"))
    print(greet(name="Rina", greeting="Welcome"))
    print(make_title("  learning python functions "))


if __name__ == "__main__":
    main()
