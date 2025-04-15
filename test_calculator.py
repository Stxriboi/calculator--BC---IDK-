# https://github.com/Stxriboi/calculator--BC---IDK-.git
# Partner 1: Bryce Cephus
# Partner 2: Bryce Cephus

import unittest
import calculator
import math

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.sub(5, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(100, 10), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-10, 2)

if __name__ == '__main__':
    unittest.main()
