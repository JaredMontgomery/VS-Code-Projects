# Exercise:
# 5. Ask the user to enter a number. Print out the square of the number, but use
# the sep optional argument to print it out in a full sentence that ends in a
# period. Sample output is shown below.

from ...utils import safe_input

num: float = safe_input("Enter a number: ", float)

print(f"The square of {num} is {num ** 2}.")
