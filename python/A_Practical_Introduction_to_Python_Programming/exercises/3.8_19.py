# Exercise:
# 19. Write a program that draws “modular rectangles” like the ones below. The
# user specifies the width and height of the rectangle, and the entries start at
# 0 and increase typewriter fashion from left to right and top to bottom, but
# are all done mod 10. Below are examples of a 3 × 5 rectangle and a 4 × 8.

from utils import safe_input

width: int = safe_input("Width of the box in chars: ", int)
height: int = safe_input("Height of the box in chars: ", int)

num: int = 0

# Prints each row.
for row in range(height):
    # Prints each number in a row:
    for column in range(width):
        print(f"{num} ", end="")

        # Prevents numbers from getting bigger than 9.
        num = (num + 1) % 10
    
    print()
