from dataclasses import dataclass


@dataclass
class Student:
    name: str
    student_id: int
    score: float


def passed(student: Student, threshold: float = 50) -> bool:
    return student.score >= threshold


def main() -> None:
    learner = Student("Ayesha", 101, 87.5)
    print(learner)
    print("Passed:", passed(learner))


if __name__ == "__main__":
    main()
