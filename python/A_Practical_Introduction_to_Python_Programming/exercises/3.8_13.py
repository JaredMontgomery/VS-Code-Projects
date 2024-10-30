# Exercise:
# 13. Write a program that asks the user for a number and then prints out the
# sine, cosine, and tangent of that number.

from math import sin, cos, tan

from utils import safe_input

num: int = safe_input("Enter a number: ", float)

print(f"sin({num}) = {sin(num)}")
print(f"cos({num}) = {cos(num)}")
print(f"tan({num}) = {tan(num)}")
