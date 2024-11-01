# Exercise:
# 6. Ask the user to enter a number x. Use the sep optional argument to print
# out x, 2x, 3x, 4x, and 5x, each separated by three dashes, like below.

from ...utils import safe_input

num: float = safe_input("Enter a number: ", float)

# Prints the first 5 multiples of [num].
for x in range(1, 6):
    print(num * x, end="---")

# Removes trailing dashes.
print("\b\b\b   ")
