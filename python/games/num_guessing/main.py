from random import randint

lower: int = int(input("Choose a lower bound: "))
upper: int = int(input("Choose a upper bound: "))

# The number that the CPU chooses.
chosen_num: int = randint(lower, upper)
# The difference between your guess and the actual number. Used to tell you when
# you're closer or further away.
num_diff: int = 0

# THe game loop.
while True:
    guess: int = int(input("Enter a guess: "))

    if guess == chosen_num:
        print("You won!\n")

        break
    elif abs(guess - chosen_num) < num_diff:
            print("Hotter.\n")
    elif abs(guess - chosen_num) > num_diff:
        print("Colder.\n")
    
    num_diff = abs(guess - chosen_num)