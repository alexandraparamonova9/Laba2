import unittest
from main import guess_number


class TestGuessNumber(unittest.TestCase):
    def setUp(self):
        self.numbers = list(range(1, 11))

    def test_guess_in_middle(self):
        result = guess_number(5, self.numbers)
        self.assertEqual(result, (5, 5))

    def test_guess_first(self):
        result = guess_number(1, self.numbers)
        self.assertEqual(result, (1, 1))

    def test_guess_last(self):
        result = guess_number(10, self.numbers)
        self.assertEqual(result, (10, 10))

if __name__ == "__main__":
    unittest.main()
