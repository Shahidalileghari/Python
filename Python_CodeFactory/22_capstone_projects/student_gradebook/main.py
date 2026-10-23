import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")


def load_students() -> list[dict[str, object]]:
    if not DATA_FILE.exists():
        return []
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Student data must be a JSON list.")
    return data


def save_students(students: list[dict[str, object]]) -> None:
    DATA_FILE.write_text(json.dumps(students, indent=2), encoding="utf-8")


def add_student(students: list[dict[str, object]], name: str, score: float) -> None:
    if not name.strip():
        raise ValueError("Name cannot be empty.")
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")
    students.append({"name": name.strip(), "score": score})


def main() -> None:
    students = load_students()
    add_student(students, "Ayesha", 91)
    save_students(students)
    average = sum(float(item["score"]) for item in students) / len(students)
    print(f"Students: {len(students)} | Average score: {average:.1f}")


if __name__ == "__main__":
    main()
