# Exercise:
# 10. a. One way to find out the last digit of a number is to mod the number by
# 10. Write a program that asks the user toenter a power. Then find the last
# digit of 2 raised to that power.

from ...utils import safe_input

num: int = safe_input("Enter a number: ", int)

print(f"The last digit of 2 ** {num} is {2 ** num % 10}.")
