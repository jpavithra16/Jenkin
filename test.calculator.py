# test_calculator.py
import unittest
from calculator import add, divide

class TestCalculator(unittest.TestCase):
    # Positive test case
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    # Negative test case (incorrect result)
    def test_add_negative(self):
        self.assertNotEqual(add(2, 2), 5)

    # Positive test for divide
    def test_divide_positive(self):
        self.assertEqual(divide(10, 2), 5)

    # Negative test case (division by zero)
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()
