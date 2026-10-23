from pathlib import Path


def main() -> None:
    output_path = Path(__file__).with_name("class_notes.txt")
    output_path.write_text(
        "Python files lesson\nRemember to close resources safely.\n",
        encoding="utf-8",
    )
    contents = output_path.read_text(encoding="utf-8")
    print(contents)


if __name__ == "__main__":
    main()
