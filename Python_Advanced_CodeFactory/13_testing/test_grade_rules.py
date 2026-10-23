import unittest


def grade(score: float) -> str:
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 80:
        return "A"
    if score >= 60:
        return "B"
    return "C"


class GradeTests(unittest.TestCase):
    def test_boundaries(self) -> None:
        self.assertEqual(grade(80), "A")
        self.assertEqual(grade(60), "B")
        self.assertEqual(grade(59.9), "C")

    def test_invalid_score(self) -> None:
        with self.assertRaises(ValueError):
            grade(101)


if __name__ == "__main__":
    unittest.main()
