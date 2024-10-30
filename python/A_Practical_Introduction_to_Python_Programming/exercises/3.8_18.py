# Exercise:
# 18. Write a program that given an amount of change less than $1.00 will print
# out exactly how many quarters, dimes, nickels, and pennies will be needed to
# efficiently make that change. [Hint: the // operator may be useful.]

from utils import safe_input

while True:
    money: int = safe_input("Enter an amount of pennies than a 100: ", int)

    if 0 <= money < 100:
        break

# Don't want to modify input, because it is needed later.
money_copy: int = money

# Calculates how many whole quarters make up a certain amount of pennies.
quarters: int = money_copy // 25
# Removes those quarters from the money amount.
money_copy %= 25

dimes: int = money_copy // 10
money_copy %= 10

nickels: int = money_copy // 5
money_copy %= 5

# Not needed, because the operations do nothing.
# pennies: int = money // 1
# money %= 1

print(f"{money} pennies to equal to {quarters} quarter(s), {dimes} dime(s), {nickels} nickel(s), and {money_copy} pennie(s).")
