# Exercise:
# 9. Write a program that asks the user for an hour between 1 and 12 and for how
# many hours in the future they want to go. Print out what the hour will be that
# many hours into the future. An example is shown below.

from utils import safe_input

hour_now: int = safe_input("Enter hour: ", int)
hours_ahead: int = safe_input("How many hours ahead? ", int)

# 12 hours after 12 is just the same time.
if hour_now == 12 and hours_ahead == 12:
    print(f"New hour: 12 o'clock")
else:
    print(f"New hour: {(hour_now + hours_ahead) % 12} o'clock")
