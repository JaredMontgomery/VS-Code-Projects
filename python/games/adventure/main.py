from rooms import *

# Where you are.
home: list[list[dict]] = [
    [bedroom, bathroom, closet],
    [empty_room, living_room, laundry_room],
    [treasure_room, kitchen, garage]
]

# Your coords in the house. First coord is the "x" and the second is "y".
pos: list[int] = [0, 0]

# What you can enter and do.
command_list: list[str] = ["up", "down", "left", "right", "ls", "see"]

# Keeps track of whether or not the magic spell to open the locked room was said.
spell_spoken: bool = False
# Keeps track of whether or not the treasure room was unlocked.
treasure_unlocked: bool = False

# Intro message.
print("Hello. This is a text adventure game. Through enough trial and error, you may be able to figure out what to do. Good luck.\n")

# The game loop.
while True:
    # Current room that you are in.
    room: dict[str, str] = home[pos[1]][pos[0]]

    print(f"You are in the {room["secret_name"]}.\n")

    if room["secret_name"] == "treasure room" and treasure_unlocked == False:
        print("Congrats! You have entered the treasure room. It contains 4 random things... Yeah, that's about it.\n")

        treasure_unlocked = True

    command: str = input("Enter a command (\"up\", \"down\", \"left\", \"right\", \"ls\", \"see\"): ").lower()

    print()

    # Handles the case of no input.
    if len(command.split()) == 0:
        print("You should enter something.\n")

        continue
    # Handles the magic spell, opening the locked room.
    elif command == "open sesame":
        spell_spoken = True

        print("You can hear a door unlocking...\n")

        continue
    elif command.split()[0] not in command_list:
        print(f"\"{command}\" is not an available command.\n")

        continue

    # Processes any entered command.
    match command.split()[0]:
        # Processes movement commands.
        case "up":
            if pos[1] > 0:
                # Moves the player up to another room.
                pos[1] -= 1
            # Prevents any IndexErrors.
            else:
                print("No room is up.\n")
        case "down":
            if pos[1] < 2:
                pos[1] += 1

                # If in the locked room, do some checks first.
                if pos == [0, 2]:
                    # If spell hasn't been spoken yet, then go out.
                    if spell_spoken == False:
                        pos[1] -= 1

                        print("The room below is locked.\n")
            else:
                print("No room is down.\n")
        case "left":
            if pos[0] > 0:
                pos[0] -= 1

                # If in the locked room, do some checks first.
                if pos == [0, 2]:
                    # If spell hasn't been spoken yet, then go out.
                    if spell_spoken == False:
                        pos[0] += 1

                        print("The room to the left is locked.\n")
            else:
                print("No room is left.\n")
        case "right":
            if pos[0] < 2:
                pos[0] += 1
            else:
                print("No room is right.\n")

        # Processes inspection commands:

        # Lists out the things in a room.
        case "ls":
            print(f"Here are some things in the {room["secret_name"]}:\n")

            for thing in room:
                if thing == "secret_name":
                    continue

                print(thing)
            
            print()
        # This shows you a description of a specific thing in a room.
        case "see":
            # Handles the hidden object in the empty room.
            if command == "see    " and pos == [0, 1]:
                print(f"{thing} description: {room[thing]}\n")

                continue
            elif len(command.split()) == 1:
                print("You must enter a thing to see.\n")

                continue

            # The thing that you want to see / inspect.
            thing: str = command.split()[1]

            if thing not in room:
                print(f"\"{thing}\" in not in the {room["secret_name"]}.\n")

                continue

            print(f"{thing} description: {room[thing]}\n")