# Exercise:
# 6. Write a program that asks the user to enter two numbers, x and y, and
# computes |x-y|/(x+y).

from utils import safe_input

x: int = safe_input("Enter a number: ", float)
y: int = safe_input("Enter another number: ", float)

print(f"abs({x} - {y}) / ({x} + {y}) == {abs(x - y) / (x + y)}")
