# Exercise:
# 14. Use for loops to print a diamond like the one below. Allow the user to
# specify how high the diamond should be.

from ...utils import safe_input

height: int = safe_input("Height of the diamond in chars: ", int)

for i in range(1, height + 1, 2):
    # Prints a number of asterisks in the center of a [height]-wide space.
    print("{0:^{w}}".format("*" * i, w=height))
