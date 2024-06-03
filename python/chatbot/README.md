The program simulates a simple chatbot. When given an input, the program searches a dictionary for the right output.
If the dictionary contains the input, then a random output for that input is given.
If the dictionary doesn't contain the input, then the program can learn fro the user what response (or responses) it should give next time.

The inputs will be stored as lowercase and won't contain any punctuation or excessive whitespace.
The outputs should be written as proper English.

# How the final program should run:

    1. Take input from the user.

    2. See if the bot knows the input. If it knows the input, then go to 3. Otherwise, go to 4.

    3. Randomly give one of the corresponding outputs for that input, then go back to 1.

    4. Ask the user to enter what response the bot should've given for the input that it didn't understand, then go back to 1.

# How the bot's inputs (user inputs) and outputs (the bot's replies to the user's inputs) should be stored:

    They should be stored in a dictionary. The inputs will be the keys and the values will be lists containing appropriate outputs for that input.
    The keys and the values in the lists will, of course, be strings. Also, the bot can have multiple outputs for a given input, so that its
    vary and aren't too repetitive or boring.

    In order for the bot to remember stuff that it has learned after the program has been closed, the dictionary should be stored in a text file.
    The next time the program is run, the dictionary will be read from the text file and put into the running program for use.

    The dictionary (that I have been talking about) is, essentially, the bot's brain and it will grow as the bot learns.

# Here's an example of a dictionary that the bot could use:

    brain = {
        "hi": ["how are you?", "greetings"],
        "bye": ["goodbye", "see you later"],
    }

When the use enter an input, the program will check to see if the input is listed as a key in the dictionary.
If it is, then the program will choose a random output from the corresponding list for that key.

If the input isn't in the dictionary, the the program will add the input as a key and the value for the key will be a list containing responses
(entered by the user) that the bot should give next time.