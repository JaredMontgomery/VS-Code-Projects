# Exercise:
# 15. Write a program that prints a giant letter A like the one below. Allow the
# user to specify how large the letter should be.

from utils import safe_input

height: int = safe_input("Height of the \"A\" in chars: ", int)

# Prints the very top point of the "A".
print("{0:^{w}}".format("*", w=(height * 2 - 1)))

# Prints the top lines of the "A".
for i in range(1, height - 2, 2):
    print("{0:^{w}}".format("*" + " " * i + "*", w=(height * 2 - 1)))

# Prints the horizontal line of the "A".
print("{0:^{w}}".format("*" * height, w=(height * 2 - 1)))

# Prints the bottom lines of the "A".
for i in range(height, height * 2 - 2, 2):
    print("{0:^{w}}".format("*" + " " * i + "*", w=(height * 2 - 1)))