# Exercise:
# 10. b. One way to find out the last two digits of a number is to mod the
# number by 100. Write a program that asks the user to enter a power. Then find
# the last two digits of 2 raised to that power.

from ...utils import safe_input

num: int = safe_input("Enter a number: ", int)

print(f"The last 2 digits of 2 ** {num} is {2 ** num % 100}.")
