# Exercise:
# 2. Write a program that generates a random number, x, between 1 and 50, a
# random number y between 2 and 5, and computes xy.

from random import random

x: int = random() * 50 + 1
y: int = random() * 3 + 2

print(f"x ({x}) to the power of y ({y}) is {x ** y}.")
