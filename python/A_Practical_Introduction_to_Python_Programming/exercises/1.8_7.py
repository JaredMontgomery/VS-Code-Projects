from utils import safe_input

kg: float = safe_input("Enter kilogram amount: ", float)

# Converts from kilograms to pounds.
print(f"{kg} kilograms is {kg * 2.2} pounds.")