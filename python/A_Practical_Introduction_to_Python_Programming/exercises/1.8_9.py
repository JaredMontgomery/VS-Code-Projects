from utils import safe_input

price: float = safe_input("Enter price: ", float)
tip: float = safe_input("Enter tip (number, not percent): ", float)

print(f"Tip amount: {price * tip}. Total: {price + price * tip}.")