# Exercise:
# 16. Below is described how to find the date of Easter in any year. Despite its
# intimidating appear- ance, this is not a hard problem. Note that bxc is the
# floor function, which for positive numbers just drops the decimal part of the
# number. For instance ⌊3.14⌋ = 3. The floor function is part of the math module.

from math import floor

from ...utils import safe_input

year: int = safe_input("Enter a year: ", int)

# These calculations are required to figure out the date of Easter... Yeah:
C = year // 100
m = (15 + C - abs(C / 4) - abs((8 * C + 13) / 25)) % 30
n = (4 + C - abs(C / 4)) % 7
a = year % 4
b = year % 7
c = year % 19
d = (19 * c + m) % 30
e = (2 * a + 4 * b + 6 * d + n) % 7

# Prints the final, calculated date.
if d == 29 and e == 6:
    print(f"Easter will fall on April 19th in {year}.")
elif d == 28 and e == 6 and m in [2, 5, 10, 13, 16, 21, 24, 39]:
    print(f"Easter will fall on April 18th in {year}.")
elif 22 + d + e <= 31:
    print(f"Easter will fall on March {floor(22 + d + e)}th in {year}.")
elif floor(d + e - 9) == 0:
    print(f"Easter will fall on April 1th in {year}.")
else:
    print(f"Easter will fall on April {floor(d + e - 9)}th in {year}.")
