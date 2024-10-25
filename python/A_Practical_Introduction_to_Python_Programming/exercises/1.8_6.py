from utils import safe_input

num: float = safe_input("Enter a number: ", float)

# Prints the first 5 multiples of [num].
for x in range(1, 6):
    print(num * x, end="---")

# Removes trailing dashes.
print("\b\b\b   ")