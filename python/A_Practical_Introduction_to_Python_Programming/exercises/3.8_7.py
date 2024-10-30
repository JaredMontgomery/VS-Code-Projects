# Exercise:
# 7. Write a program that asks the user to enter an angle between -180° and
# 180°. Using an expression with the modulo operator, convert the angle to its
# equivalent between 0° and 360°.

from utils import safe_input

while True:
    angle: float = safe_input("Enter a an angle between -180 and 180 degrees: ", float)

    if -180 <= angle <= 180:
        break

print(f"{angle} degrees is equal to {(angle + 360) % 360} degrees.")
