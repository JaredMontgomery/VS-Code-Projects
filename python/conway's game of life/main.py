from random import choices
from time import sleep


def make_empty_grid(
        columns: int,
        rows: int,

        edge_char: str = "#",
        fill_char: str = " ",
    ) -> list:

    """Creates an empty grid (full of fill_char) with a certain number of columns and rows.

    The grid will also have an outline of edge_char, which will act as a wall.
    """

    grid = []

    # This block fills the grid with stuff.
    grid.append(list(edge_char * columns))  # Top wall.

    # The rows between the top and bottom wall.
    # Also includes everything for the left and right walls.
    for i in range(rows - 2):
        grid.append(list(edge_char + fill_char*(columns - 2) + edge_char))

    grid.append(list(edge_char * columns))  # Bottom wall.

    return grid


def make_random_grid(
        columns: int,
        rows: int,

        edge_char: str = "#",
        fill_char: str = " ",  # Can also represent an empty or dead cell.

        alive_char: str = "█",
        alive_chance: int = 50,
    ) -> list:

    """Creates an randomized grid with a certain number of columns and rows.

    The grid will also have an outline of edge_char, which will act as a wall.

    alive_chance is the chance (as a percentage) that a cell will be alive.
    """

    from random import choices

    grid = []

    # This block fills the grid with stuff.
    grid.append(list(edge_char * columns))  # Top wall.

    # The rows between the top and bottom wall.
    # Also includes everything for the left and right walls.
    for i in range(rows - 2):
        row = choices([alive_char, fill_char], [alive_chance, 100 - alive_chance], k=(columns - 2))
        grid.append([edge_char] + row + [edge_char])

    grid.append(list(edge_char * columns))  # Bottom wall.

    return grid


def print_grid(
        grid: list,
    ) -> None:

    """Prints a grid in a nice way."""

    for row in grid:
        print(*row)
    
    print()


def count_neighbors(
        x: int,
        y: int,
        main_grid: list,
        alive_char: str = "█",
    ) -> int:

    """Counts the (living) neighbors around a certain point (x, y) in a grid (main_grid).
    
    A neighbor is considered living if it is alive_char.
    """

    neighbors_num = 0

    # Top neighbors.
    if main_grid[y - 1][x - 1] == alive_char:  # Top left.
        neighbors_num += 1
    if main_grid[y - 1][x] == alive_char:  # Top middle.
        neighbors_num += 1
    if main_grid[y - 1][x + 1] == alive_char:  # Top right.
        neighbors_num += 1

    # Side neighbors (to the left and right).
    if main_grid[y][x - 1] == alive_char:  # Left.
        neighbors_num += 1
    if main_grid[y][x + 1] == alive_char:  # Right.
        neighbors_num += 1

    # Bottom neighbors.
    if main_grid[y + 1][x - 1] == alive_char:  # Bottom left.
        neighbors_num += 1
    if main_grid[y + 1][x] == alive_char:  # Bottom middle.
        neighbors_num += 1
    if main_grid[y + 1][x + 1] == alive_char:  # Bottom right.
        neighbors_num += 1
    
    return neighbors_num


def apply_rules(
        cell: str,
        neighbors_num: int,

        x: int,
        y: int,

        updated_grid: list,

        alive_char: str = "█",
        dead_char: str = " ",

        birth_rule: list = [3],
        live_rule: list = [2, 3],
    ) -> list:

    """Takes a cell at (x, y) with neighbors_num neighbors, applies the game rules to it,
    and saves the resulting cell into updated_grid.

    A cell is alive if it is alive_char and dead if it is dead_char.

    birth_rule is a list of numbers. Each number represent how many neighbors a dead cell
    needs in order to come to life in the next generation.

    live_rule is a list of numbers. Each number represents how many neighbors a living
    cell needs in order to stay alive for the next generation.
    """

    if cell == alive_char:
        if neighbors_num in live_rule:
            updated_grid[y][x] = alive_char
        else:
            updated_grid[y][x] = dead_char
    else:
        if neighbors_num in birth_rule:
            updated_grid[y][x] = alive_char

    return updated_grid


def correct_input(
        func,
        error_message: str = "Wrong input. Try again.",
    ):

    """Tries to make sure that the user corrects some correct input.

    It is intended that func is a function that takes user input
    (usually with the built-in input() function).

    It's also intended that func will provide some sort of text so that
    the user knows what to enter (usually done with a prompt in the
    built-in input() function).

    func can raise an exception if user input is not what is expected,
    which will be handled in this function.
    
    Also, if an error occurs,
    then a custom error message can be printed.
    """

    while True:
        try:
            input_var = func()
        except:
            print(error_message)
        else:
            return input_var


def make_generation(
        main_grid: list,

        columns: int = 20,
        rows: int = 20,

        alive_char: str = "█",
        dead_char: str = " ",

        birth_rule: list = [3],
        live_rule: list = [2, 3],
    ) -> list:
    """Creates a new generation for a grid.
    
    A cell is alive if it is alive_char and dead if it is dead_char.

    birth_rule is a list of numbers. Each number represent how many neighbors a dead cell
    needs in order to come to life in the next generation.

    live_rule is a list of numbers. Each number represents how many neighbors a living
    cell needs in order to stay alive for the next generation.
    """

    updated_grid = make_empty_grid(columns, rows)

    for y in range(1, len(main_grid) - 1):
        for x in range(1, len(main_grid[0]) - 1):
            cell = main_grid[y][x]

            neighbors_num = count_neighbors(x, y, main_grid)

            updated_grid = apply_rules(
                cell,
                neighbors_num,

                x,
                y,

                updated_grid,

                alive_char,
                dead_char,

                birth_rule,
                live_rule
            )

    # main_grid = updated_grid.copy()

    return updated_grid


def main():
    """Contains all of the code for the game."""
    
    # The next 3 blocks define some constants.

    # Constants for the grid.
    if correct_input(lambda: input("Enter numbers for column and row amounts? (y / Y for yes, anything else for no): ").lower()) == 'y':
        COLUMNS = correct_input(
            lambda: int(input("Enter a number for the amount of columns: ")),
            error_message="Please enter a valid integer."
        )
        ROWS = correct_input(
            lambda: int(input("Enter a number for the amount of rows: ")),
            error_message="Please enter a valid integer."
        )
    else:
        COLUMNS, ROWS = 20, 20
    SPEED = 4

    # Constants for displayed characters.
    ALIVE_CHAR = "█"
    DEAD_CHAR = " "

    # Constants for the rules of the game.
    #
    # Default rules for the game of life:
    # BIRTH_RULE = [3]
    # LIVE_RULE = [2, 3]
    #
    # BIRTH_RULE determines how many neighbors are needed for a dead cell to come to life.
    # LIVE_RULE determines how many neighbors are needed for a living cell to stay alive.
    BIRTH_RULE = [3]
    LIVE_RULE = [2, 3]

    if correct_input(lambda: input("Empty or randomized grid? (e / E for empty, anything else for randomized): ").lower()) == "e":
        main_grid = make_empty_grid(COLUMNS, ROWS)

        # Makes a glider in the top left.
        main_grid[1][2] = ALIVE_CHAR
        main_grid[2][3] = ALIVE_CHAR
        main_grid[3][3] = ALIVE_CHAR
        main_grid[3][2] = ALIVE_CHAR
        main_grid[3][1] = ALIVE_CHAR
    else:
        if correct_input(lambda: input("Enter a number for the percent chance? (y / Y for yes, anything else for 50%): ").lower()) == "y":
            alive_chance = correct_input(
                lambda: float(input("Enter a number for the percent chance that a cell should be alive: ")),
                error_message="Please enter a valid number."
            )
        else:
            alive_chance = 50

        main_grid = make_random_grid(COLUMNS, ROWS, alive_chance=alive_chance)
        del alive_chance

    # The main "game" loop.
    while True:
        # "Draws" a "frame".
        print_grid(main_grid)

        main_grid = make_generation(main_grid, COLUMNS, ROWS)

        sleep(1 / SPEED)


if __name__ == "__main__":
    main()