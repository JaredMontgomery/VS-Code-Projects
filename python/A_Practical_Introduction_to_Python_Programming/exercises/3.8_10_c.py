# Exercise:
# 10. c. Write a program that asks the user to enter a power and how many digits
# they want. Find the last that many digits of 2 raised to the power the user
# entered.

from ...utils import safe_input

num: int = safe_input("Enter a number: ", int)
digits: int = safe_input("How many last digits do you want? ", int)

print(f"The last {digits} digits of 2 ** {num} is {2 ** num % 10 ** digits}.")
