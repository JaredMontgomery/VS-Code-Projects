from random import choice


def main() -> None:
    """
    Allows a conversation between you and the brain.
    """

    brain: dict = open_brain()

    # Main loop. Used to repeatedly allow back-and-forth messaging.
    while True:
        user_input = input("Enter an input to talk (or n to end program): ")

        # The program will end when the user enters "q" (for quit).
        if handle_input(user_input, brain) == "q":
            break


def open_brain() -> dict:
    """
    Opens the brain.txt file if it can found. Otherwise, a default brain is
    used.

    Time complexity - O(1).
    Space complexity - O(N), where N is the number of items in the brain dict.
    """

    # Tries to open the brain file.
    try:
        brain_file = open("brain.txt", "r")
        # eval takes the string rep of the brain.txt dict and turns it into an
        # actual dict.
        brain = eval(brain_file.read())
        brain_file.close()
    # If the brain file couldn't be found, then a default brain will be used as
    # said below.
    except OSError:
        print("brain.txt couldn't be found. Default brain dict will be used.")

        brain_file = open("brain.txt", "w")

        brain = {
            "hi": ["Hello.", "Greetings.", "What's up?"],
            "bye": ["Goodbye.", "Farewell.", "See you later."],

            "how are you": ["I'm fine.", "Alright.", "Okay."],
            "hotel": ["trivago"],
        }

        brain_file.write(str(brain))
        brain_file.close()
    
    return brain


def handle_input(user_input: str, brain: dict) -> str | None:
    """
    Handles input for the brain.

    If the user enters "q" (for quit), then the function ends.
    If not, then the brain will look for an appropriate response to the input.
    If a reponse can't be found, then you will have to teach it what to say.
    """

    # Used to quit.
    if user_input == "q":
        return "q"
    # Looks up message in the brain and gives a response to it.
    elif user_input in brain:
        print(choice(brain[user_input]))
    # If message isn't in the brain, then it will have to learn responses.
    else:
        learn(user_input, brain)


def learn(user_input: str, brain: dict) -> None:
    """
    Education and learning. The brain will repeatedly ask for responses to a
    given input. The next time the brain is given that input, it will randomly
    give one of the learned responses.
    """

    # If the input isn't in dict, then make a place for it and its outputs.
    brain[user_input] = []

    # Adds an initial output.
    learned_input = input(
        "I don't know what you mean. Please enter what I should say: "
    )
    brain[user_input].append(learned_input)

    # Gets more outputs if wanted by the user.
    while True:
        learned_input = input(
            "Any other response I should know? (n for no or enter the response): "
        )

        if learned_input == "q":
            break
        else:
            brain[user_input].append(learned_input)
    
    # The updated brain will be saved in brain.txt.
    brain_file = open("brain.txt", "w")
    brain_file.write(str(brain))
    brain_file.close()


if __name__ == "__main__":
    main()