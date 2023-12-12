#discount_calculator.py

class DiscountCalculator:
    def calculate_discount(volume):
        if volume >= 1000:
            return 0.1
        if volume >= 500:
            return 0.05
        else:
            return 0.0
        
print(DiscountCalculator.calculate_discount(1000))
print(DiscountCalculator.calculate_discount(500))
print(DiscountCalculator.calculate_discount(1))