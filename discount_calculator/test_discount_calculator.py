import unittest
from discount_calculator import calculate_discount

class DiscountCalculatorTest(unittest.TestCase):

    def test_calculate_discount_input(self):
        for i in range(0, 499):
            self.assertEqual(calculate_discount(i), 0.0, "Failed for volume 0")
        for i in range(500, 999):
            self.assertEqual(calculate_discount(i), 0.05, "Failed for volume 500")
        for i in range(1000, 1500):
            self.assertEqual(calculate_discount(i), 0.1, "Failed for volume 1000")

if __name__=='__main__':
    unittest.main()


    # def setUp(self):
    #     self.val = 499

    # def test_discount_calculator1(self):
    #     self.assertEqual(DiscountCalculator.calculate_discount(1000), 0.1, "Failed for volume 1000")

    # def test_discount_calculator05(self):
    #     self.assertEqual(DiscountCalculator.calculate_discount(500), 0.05, "Failed for volume 500")

    # def test_discount_calculator0(self):
    #     actual_discount = DiscountCalculator.calculate_discount(self.val)
    #     expected_discount = 0.0
    #     self.assertEqual(actual_discount, expected_discount, "Failed for volume 0")