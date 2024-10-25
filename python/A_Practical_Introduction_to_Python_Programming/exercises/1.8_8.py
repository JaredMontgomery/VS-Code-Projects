from utils import safe_input

total: float = 0
# Amount of numbers to add up.
amount: int = 3

# Adds up 3 numbers from the user.
for i in range(1, amount + 1):
    total += safe_input(f"Enter number {i}: ", float)

print(f"Total: {total}. Average: {total / amount}.")