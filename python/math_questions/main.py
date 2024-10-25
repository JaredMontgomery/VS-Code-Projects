from random import choice, randint

from utils import safe_input

print("Modes: 1 for easy, 2 for hard, 3 for extreme, or any other number.")
difficulty: int = safe_input("Enter a difficulty: ", int)

# Number of times you can answer wrong.
lives: int = 1

if difficulty < 4:
    lives = 2 ** (4 - difficulty) - 1

score: int = 0

# Amount of questions answered.
question_amount: int = 0

# Available operations to use in questions.
ops: list = [
    "+", '-', "*", "//", # "%",
    # "^", "&", "|",
    # ">", "<", ">=", "<=", "==", "!="
]

# The game loop. Goes until you lose.
while lives != 0:
    # Picks 2 numbers. Their lengths on based on the difficulty. For example, a
    # difficulty of 1 gives 1 digits numbers, a difficulty of 2 gives 2 digit
    # numbers and so on.
    num_1: int = randint(10 ** (difficulty - 1), 10 ** difficulty - 1)
    num_2: int = randint(10 ** (difficulty - 1), 10 ** difficulty - 1)

    # Randomly chooses an operation.
    chosen_op: str = choice(ops)

    expression: str = f"{num_1} {chosen_op} {num_2}"
    right_answer: int = eval(expression)

    question_amount += 1

    # Prompts the user for an answer.
    user_answer: int = safe_input(f"{question_amount}. What's {expression}?\n", int)

    # If correct, then the player is rewarded with points. The harder the
    # question, the bigger the reward.
    if user_answer == right_answer:
        score += 100 * difficulty

        print(f"Right. Score: {score}. Lives: {lives}.\n")
    # If wrong, then score and lives are decremented.
    else:
        score -= 100 * difficulty
        lives -= 1

        print(f"Wrong. Score: {score}. Lives: {lives}. Right answer: {right_answer}.\n")

print("You lose.")