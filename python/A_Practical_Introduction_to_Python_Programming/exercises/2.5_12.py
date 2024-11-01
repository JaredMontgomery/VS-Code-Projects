# Exercise:
# 12. Use a for loop to print a triangle like the one below. Allow the user to
# specify how high the triangle should be.

from ...utils import safe_input

height: int = safe_input("Height of the left-aligned triangle in chars: ", int)

for i in range(1, height + 1):
    print("*" * i)
