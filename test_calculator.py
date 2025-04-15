# https://github.com/Stxriboi/lab10--BC---IDK-.git
# Partner 1: Bryce Cephus
# Partner 2: N/A

import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(4, 2), 8)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            calculator.divide(5, 0)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)

    def test_mod(self):
        self.assertEqual(calculator.mod(10, 3), 1)

if __name__ == '__main__':
    unittest.main()
