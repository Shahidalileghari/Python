from datetime import date
from pathlib import Path
import random


def main() -> None:
    print("Today:", date.today())
    print("Random practice number:", random.randint(1, 10))
    print("Current folder name:", Path.cwd().name)


if __name__ == "__main__":
    main()
