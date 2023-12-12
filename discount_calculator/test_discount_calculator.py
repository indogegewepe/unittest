import unittest
from discount_calculator import DiscountCalculator

class DiscountCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.val1 = 1000129308109283
        self.val05 = 999
        self.val0 = 499

    def test_discount_calculator1(self):
        self.assertEqual(DiscountCalculator.calculate_discount(self.val1), 0.1, "Failed for volume 1000")

    def test_discount_calculator05(self):
        self.assertEqual(DiscountCalculator.calculate_discount(self.val05), 0.05, "Failed for volume 500")

    def test_discount_calculator0(self):
        actual_discount = DiscountCalculator.calculate_discount(self.val0)
        expected_discount = 0.0
        self.assertEqual(actual_discount, expected_discount, "Failed for volume 0")

if __name__=='__main__':
    unittest.main()