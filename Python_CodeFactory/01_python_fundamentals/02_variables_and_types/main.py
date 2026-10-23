def main() -> None:
    student_name: str = "Ayesha"
    student_age: int = 19
    course_fee: float = 12500.50
    is_enrolled: bool = True

    print(student_name, type(student_name).__name__)
    print(student_age, type(student_age).__name__)
    print(course_fee, type(course_fee).__name__)
    print(is_enrolled, type(is_enrolled).__name__)


if __name__ == "__main__":
    main()
