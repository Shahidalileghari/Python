import os


def validate_username(value: str) -> str:
    cleaned = value.strip()
    if not cleaned or len(cleaned) > 30:
        raise ValueError("Username must contain 1 to 30 characters.")
    return cleaned


def main() -> None:
    username = validate_username("  student_01  ")
    print("Validated username:", username)

    # Read secrets from environment rather than hard-coding them.
    # Example: set APP_TOKEN in your shell before running a real app.
    token = os.getenv("APP_TOKEN")
    print("APP_TOKEN configured:", token is not None)
    # Never print the token itself or commit it to Git.


if __name__ == "__main__":
    main()
