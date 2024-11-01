# Exercise:
# 8. Write a program that asks the user for their name and how many times to
# print it. The program should print out the user's name the specified number of
# times.

from ...utils import safe_input

name: str = input("Enter your name: ")
num: int = safe_input("Enter amount of times to print: ", int)

for i in range(1, num + 1):
    print(f"{i}. {name}.")
