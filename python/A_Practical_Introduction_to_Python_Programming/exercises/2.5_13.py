# Exercise:
# 13. Use a for loop to print an upside down triangle like the one below. Allow
# the user to specify how high the triangle should be.

from utils import safe_input

height: int = safe_input("Height of the upside-down, left-aligned triangle in chars: ", int)

for i in range(height, 0, -1):
    print("*" * i)
