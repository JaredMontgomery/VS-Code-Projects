# Exercise:
# 17. A year is a leap year if it is divisible by 4, except that years divisible
# by 100 are not leap years unless they are also divisible by 400. Ask the user
# to enter a year, and, using the // operator, determine how many leap years
# there have been between 1600 and that year.

from ...utils import safe_input

year: int = safe_input("Enter a year: ", int)

if year % 100 == 0:
    if year % 400 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap year.")
