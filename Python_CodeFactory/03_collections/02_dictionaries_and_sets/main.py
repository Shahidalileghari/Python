def main() -> None:
    student = {"name": "Ayesha", "score": 91}
    student["passed"] = student["score"] >= 50
    print(student["name"], "passed:", student["passed"])

    tags = {"python", "beginner", "python"}
    print("Unique tags:", tags)
    print("Has python?", "python" in tags)


if __name__ == "__main__":
    main()
