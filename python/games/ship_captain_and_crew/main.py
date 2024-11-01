from random import randint

# Very customizable as you can see.
player_amount: int = int(input("How many players? (Default: 2). "))
roll_amount: int = int(input("How many rolls per player? (Default: 3). "))
dice_amount: int = int(input("How many dice per player? (Default: 5). "))

# A list of lists. Each inner list holds the die numbers that a player needs to
# get. 6 for the "ship", 5 for the "captain", and 4 for the "crew".
player_crews: list[list[int]] = [[6, 5, 4]] * player_amount
# Holds the scores of every player.
player_scores: list[int] = [0] * player_amount

# Let's each player have their turn.
for player_num in range(1, player_amount + 1):
    # Rolls all of a player's dice.
    for roll_num in range(1, roll_amount + 1):
        print(f"\nPlayer {player_num} will roll 5 dice. This is roll {roll_num}.")

        input(f"Press any key to roll the 5 dice.\n")
        
        # Rolls one die at a time.
        for die_num in range(1, dice_amount + 1):

            result: int = randint(1, 6)

            print(f"Player {player_num} rolled a {result}.")

            # If a player collected the ship, captain, and crew, then any
            # further numbers are added to their score.
            if len(player_crews[player_num - 1]) == 0:
                player_scores[player_num - 1] += result

                print(f"Player {player_num}'s score: {player_scores[player_num - 1]}")
            # Handles what happens when a player gets a ship, captain, or crew.
            elif result == player_crews[player_num - 1][0]:
                match result:
                    case 6:
                        print(f"Player {player_num} got the ship.")
                    case 5:
                        print(f"Player {player_num} got the captain.")
                    case 4:
                        print(f"Player {player_num} got the crew.")
                
                del player_crews[player_num - 1][0]

highest_score: int = max(player_scores)
highest_score_players: list[int] = []

# Gets the number of every player that has the highest score.
for player_num in range(len(player_scores)):
    if player_scores[player_num] == highest_score:
        highest_score_players.append(player_num)

# If only one has the max score, then they win.
if len(highest_score_players) == 1:
    print(f"\nPlayer {highest_score_players[0] + 1} won!")
# Otherwise, there are ties.
else:
    print("\nPlayers ", end="")

    # Prints out the number of every player that tied.
    for player_num in highest_score_players[:-1]:
        print(f"{player_num + 1}, ", end="")
    
    print(f"and {highest_score_players[-1] + 1} tied!")

print(f"Their score: {highest_score}.\n")