import csv
import json
from pathlib import Path


def main() -> None:
    folder = Path(__file__).parent
    records = [
        {"name": "Ayesha", "score": 91},
        {"name": "Ali", "score": 84},
    ]

    json_path = folder / "students.json"
    json_path.write_text(json.dumps(records, indent=2), encoding="utf-8")
    print(json_path.read_text(encoding="utf-8"))

    csv_path = folder / "students.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "score"])
        writer.writeheader()
        writer.writerows(records)
    print("Wrote JSON and CSV files.")


if __name__ == "__main__":
    main()
