import unittest


def is_even(number: int) -> bool:
    return number % 2 == 0


class TestIsEven(unittest.TestCase):
    def test_even_number(self) -> None:
        self.assertTrue(is_even(8))

    def test_odd_number(self) -> None:
        self.assertFalse(is_even(7))

    def test_zero_is_even(self) -> None:
        self.assertTrue(is_even(0))


if __name__ == "__main__":
    unittest.main()
