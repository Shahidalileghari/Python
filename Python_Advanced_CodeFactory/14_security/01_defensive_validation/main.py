import os
import re

USERNAME = re.compile(r"^[A-Za-z][A-Za-z0-9_]{2,19}$")


def validate_username(value: str) -> str:
    if not USERNAME.fullmatch(value):
        raise ValueError("Use 3–20 letters, digits, or underscores; start with a letter")
    return value


if __name__ == "__main__":
    print("Valid:", validate_username("student_01"))
    print("DEMO_API_KEY configured:", bool(os.getenv("DEMO_API_KEY")))
    # Never print secret values or commit credentials.
