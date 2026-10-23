def grade_for(score: float) -> str:
    if not 0 <= score <= 100:
        return "Invalid score"
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def main() -> None:
    for score in (95, 84, 73, 62, 42, 120):
        print(score, "->", grade_for(score))


if __name__ == "__main__":
    main()
