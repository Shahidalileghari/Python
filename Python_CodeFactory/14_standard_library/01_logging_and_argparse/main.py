import argparse
import logging


def main() -> None:
    parser = argparse.ArgumentParser(description="A small greeting tool.")
    parser.add_argument("--name", default="student", help="Name to greet")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logging.info("Preparing greeting")
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
