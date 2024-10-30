# Exercise:
# 1. Write a program that generates and prints 50 random integers, each between
# 3 and 6.

from random import randint

print("50 random integers:")

for i in range(1, 51):
    print(f"{i}. {randint(3, 6)}")
