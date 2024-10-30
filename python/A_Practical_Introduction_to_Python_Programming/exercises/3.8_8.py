# Exercise:
# 8. Write a program that asks the user for a number of seconds and prints out
# how many minutes and seconds that is. For instance, 200 seconds is 3 minutes
# and 20 seconds. [Hint: Use the // operator to get minutes and the % operator
# to get seconds.]

from utils import safe_input

seconds: float = safe_input("Enter a number of seconds: ", float)

print(f"{seconds} second(s) is equal to {seconds // 60} minute(s) and {seconds % 60} second(s).")
