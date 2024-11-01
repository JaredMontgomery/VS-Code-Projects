# Exercise:
# 9. A lot of cell phones have tip calculators. Write one. Ask the user for the
# price of the meal and the percent tip they want to leave. Then print both the
# tip amount and the total bill with the tip included.

from ...utils import safe_input

price: float = safe_input("Enter price: ", float)
tip: float = safe_input("Enter tip (number, not percent): ", float)

print(f"Tip amount: {price * tip}. Total: {price + price * tip}.")
