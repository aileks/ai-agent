import unittest
from pkg.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.evaluate("3 + 5"), 8.0)
        self.assertEqual(self.calculator.evaluate("10 + 0"), 10.0)
        self.assertEqual(self.calculator.evaluate("-5 + 5"), 0.0)

    def test_subtraction(self):
        self.assertEqual(self.calculator.evaluate("10 - 5"), 5.0)
        self.assertEqual(self.calculator.evaluate("5 - 10"), -5.0)
        self.assertEqual(self.calculator.evaluate("0 - 0"), 0.0)

    def test_multiplication(self):
        self.assertEqual(self.calculator.evaluate("3 * 5"), 15.0)
        self.assertEqual(self.calculator.evaluate("10 * 0"), 0.0)
        self.assertEqual(self.calculator.evaluate("-2 * 4"), -8.0)

    def test_division(self):
        self.assertEqual(self.calculator.evaluate("10 / 2"), 5.0)
        self.assertEqual(self.calculator.evaluate("1 / 2"), 0.5)
        self.assertEqual(self.calculator.evaluate("10 / 4"), 2.5)

    def test_order_of_operations(self):
        self.assertEqual(self.calculator.evaluate("3 + 5 * 2"), 13.0)
        self.assertEqual(self.calculator.evaluate("10 - 4 / 2"), 8.0)
        self.assertEqual(self.calculator.evaluate("2 * 3 + 4 / 2"), 8.0)
        self.assertEqual(self.calculator.evaluate("2 + 2 * 2 - 2 / 2"), 5.0)

    def test_complex_expressions(self):
        self.assertEqual(self.calculator.evaluate("10 + 2 * 6 - 4 / 2"), 20.0)
        self.assertEqual(self.calculator.evaluate("5 * 5 - 10 / 2 + 3"), 23.0)

    def test_invalid_expressions(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("3 +")
        with self.assertRaises(ValueError):
            self.calculator.evaluate("+ 3")
        with self.assertRaises(ValueError):
            self.calculator.evaluate("3 5")
        with self.assertRaises(ValueError):
            self.calculator.evaluate("3 + * 5")
        with self.assertRaises(ValueError):
            self.calculator.evaluate("abc")

    def test_empty_and_whitespace_expressions(self):
        self.assertIsNone(self.calculator.evaluate(""))
        self.assertIsNone(self.calculator.evaluate("   "))

if __name__ == '__main__':
    unittest.main()