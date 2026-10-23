from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


def positive_integers(path: Path) -> Iterator[int]:
    with path.open(encoding="utf-8") as source:
        for line_number, raw in enumerate(source, start=1):
            value = raw.strip()
            if not value:
                continue
            try:
                number = int(value)
            except ValueError as error:
                raise ValueError(f"Invalid integer on line {line_number}") from error
            if number > 0:
                yield number


@contextmanager
def temporary_file(path: Path) -> Iterator[Path]:
    try:
        path.write_text("4\n7\n11\n", encoding="utf-8")
        yield path
    finally:
        path.unlink(missing_ok=True)


if __name__ == "__main__":
    path = Path(__file__).with_name("numbers.tmp")
    with temporary_file(path) as source:
        print("Total:", sum(positive_integers(source)))
    print("Removed:", not path.exists())
