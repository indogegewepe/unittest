#discount_calculator.py

def calculate_discount(volume):
    if volume >= 1000:
        return 0.1
    elif volume >= 500:
        return 0.05
    else:
        return 0.0

for i in range(0, 1500):
    print(calculate_discount(i))

# print(calculate_discount(1000))
# print(calculate_discount(500))
# print(calculate_discount(1))