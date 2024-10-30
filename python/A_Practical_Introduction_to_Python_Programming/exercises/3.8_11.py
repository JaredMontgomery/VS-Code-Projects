# Exercise:
# 11. Write a program that asks the user to enter a weight in kilograms. The
# program should convert it to pounds, printing the answer rounded to the
# nearest tenth of a pound.

from utils import safe_input

kg: float = safe_input("Enter kilogram amount: ", float)

# Converts from kilograms to pounds.
print(f"{kg} kilograms is {round(kg * 2.2, 1)} pounds.")
