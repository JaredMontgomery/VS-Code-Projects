# Exercise:
# 10. Use a for loop to print a box like the one below. Allow the user to
# specify how wide and how high the box should be. [Hint: print('*' * 10) prints
# ten asterisks.]

from utils import safe_input

width: int = safe_input("Width of the box in chars: ", int)
height: int = safe_input("Height of the box in chars: ", int)

for i in range(height):
    print("#" * width)
