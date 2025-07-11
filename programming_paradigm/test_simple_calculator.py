# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0) # Another simple test case

    def test_subtract(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, 5), -3) # Another simple test case

    def test_multiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-4, 5), -20) # Another simple test case

    def test_divide_normal(self):
        """Test the division method with normal inputs."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(10, 4), 2.5) # Test with a float result

    def test_divide_by_zero(self):
        """Test the division method with division by zero."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0)) # Edge case: 0 divided by 0

if __name__ == '__main__':
    unittest.main()