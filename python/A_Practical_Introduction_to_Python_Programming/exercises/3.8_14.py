# Exercise:
# 14. Write a program that asks the user to enter an angle in degrees and prints
# out the sine of that angle.

from math import sin

from ...utils import safe_input

num: int = safe_input("Enter a number: ", float)

print(f"sin({num}) = {sin(num)}")
