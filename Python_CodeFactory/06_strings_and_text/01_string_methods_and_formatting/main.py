def main() -> None:
    raw_text = "  Python, clean code, testing  "
    cleaned = raw_text.strip()
    topics = [part.strip() for part in cleaned.split(",")]

    print(cleaned.upper())
    print("Topics:", topics)
    print(f"There are {len(cleaned)} characters in the cleaned text.")


if __name__ == "__main__":
    main()
