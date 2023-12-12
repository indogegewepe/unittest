import unittest
from discount_calculator import DiscountCalculator

class DiscountCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.val1 = 1000
        self.val05 = 500
        self.val0 = 1

    def test_discount_calculator1(self):
        actual_discount = DiscountCalculator.calculate_discount(self.val1)
        expected_discount = 0.1
        self.assertEqual(actual_discount, expected_discount)

    def test_discount_calculator05(self):
        actual_discount = DiscountCalculator.calculate_discount(self.val05)
        expected_discount = 0.05
        self.assertEqual(actual_discount, expected_discount)

    def test_discount_calculator0(self):
        actual_discount = DiscountCalculator.calculate_discount(self.val0)
        expected_discount = 0.0
        self.assertEqual(actual_discount, expected_discount)

unittest.main()