# https://github.com/Stxriboi/calculator--BC---IDK-.git
# Partner 1: Bryce Cephus
# Partner 2: Bryce Cephus

import unittest
import calculator
import math

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(calculator.sub(10, 4), 6)

    def test_mul(self):
        self.assertEqual(calculator.mul(3, 7), 21)

    def test_div(self):
        self.assertEqual(calculator.div(20, 5), 4)
        with self.assertRaises(ValueError):
            calculator.div(10, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(100, 10), 2)

    def test_exp(self):
        self.assertEqual(calculator.exp(2, 3), 8)

    def test_square_root(self):
        self.assertAlmostEqual(calculator.square_root(25), 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)

if __name__ == '__main__':
    unittest.main()
