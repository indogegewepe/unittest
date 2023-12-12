#discount_calculator.py

def calculate_discount(volume):
    if volume >= 1000:
        return 0.1
    if volume >= 500:
        return 0.05
    else:
        return 0.0