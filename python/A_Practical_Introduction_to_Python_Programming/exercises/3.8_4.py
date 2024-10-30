# Exercise:
# 4. Write a program that generates a random decimal number between 1 and 10
# with two decimal places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00.

from random import randint

print("A random number between 1 and 10:")

print(randint(100, 1000) / 100)
