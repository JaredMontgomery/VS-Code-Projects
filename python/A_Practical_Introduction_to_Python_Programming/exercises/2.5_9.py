# Exercise:
# 9. The Fibonacci numbers are the sequence below, where the first two numbers
# are 1, and each number thereafter is the sum of the two preceding numbers.
# Write a program that asks the user how many Fibonacci numbers to print and
# then prints that many.

from utils import safe_input

num: int = safe_input("Enter amount of Fibonacci numbers to print: ", int)

first = 1
second = 1

for i in range(1, num + 1):
    print(f"{i}. {first}")

    next = first + second

    # Shifts everything to the left.
    first = second
    second = next
