# Exercise:
# 11. Use a for loop to print a box like the one below. Allow the user to
# specify how wide and how high the box should be.

from ...utils import safe_input

width: int = safe_input("Width of the box in chars: ", int)
height: int = safe_input("Height of the box in chars: ", int)

# Top row.
print("#" * width)

for i in range(height - 2):
    # Empty rows on the inside.
    print("#" + " " * (width - 2) + "#")
    
# Bottom row.
print("#" * width)
