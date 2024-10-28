# Exercise:
# 8. Write a program that asks the user to enter three numbers (use three
# separate input statements). Create variables called total and average that
# hold the sum and average of the three numbers and print out the values of
# total and average.

from utils import safe_input

total: float = 0
# Amount of numbers to add up.
amount: int = 3

# Adds up 3 numbers from the user.
for i in range(1, amount + 1):
    total += safe_input(f"Enter number {i}: ", float)

print(f"Total: {total}. Average: {total / amount}.")
