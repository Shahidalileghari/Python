import argparse
import os


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Advanced CodeFactory greeting CLI")
    parser.add_argument("--name", default="student")
    parser.add_argument("--uppercase", action="store_true")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    environment = os.getenv("APP_ENV", "development")
    message = f"Hello, {args.name.strip() or 'student'}!"
    print(message.upper() if args.uppercase else message)
    print(f"Environment: {environment}")


if __name__ == "__main__":
    main()
