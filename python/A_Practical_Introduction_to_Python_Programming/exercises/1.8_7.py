# Exercise:
# 7. Write a program that asks the user for a weight in kilograms and converts
# it to pounds. There are 2.2 pounds in a kilogram.

from utils import safe_input

kg: float = safe_input("Enter kilogram amount: ", float)

# Converts from kilograms to pounds.
print(f"{kg} kilograms is {kg * 2.2} pounds.")
