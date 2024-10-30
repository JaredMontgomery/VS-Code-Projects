# Exercise:
# 15. Write a program that prints out the sine and cosine of the angles ranging
# from 0 to 345° in 15° increments. Each result should be rounded to 4 decimal
# places. Sample output is shown below:

from math import sin, cos, pi

for i in range(0, 360, 15):
    # Must convert from degrees to radians first.
    radians: float = (i * pi) / 180

    print(f"{i} --- {round(sin(radians), 4)} {round(cos(radians), 4)}")
