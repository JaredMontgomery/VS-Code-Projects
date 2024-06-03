This program simulates John Conway's Game of Life.

The GOL is what is called a cellular automaton. Basically, it's a simulation that
runs automatically on cells.

The GOL consists of a grid of cells (squares) and rules are applied to each cell
in the grid.

The GOL has 4 simple rules:
    The following 3 rules apply to living cells:
        1. If a living cell has under 2 neighbors, then the living cell will die
        in the next generation (from starvation, you could say).

        2. If a living cell has 2 or 3 neighbors, then the living cell will stay
        alive in the next generation.

        3. If a living cell has more than 3 neighbors, then the living cell will
        die in the next generation.
    The following 1 rule applys to dead cells:
        4. If a dead cell has exactly 3 neighbors, then the cell will come to
        life in the next generation.

Btw, here's some terminology explained:

1. Cellular automaton:
    Something (like a simulation of rules) that runs automatically (automaton) on
    cells (cellular). Also, the plural of "automaton" is "automata".

2. Living (of a cell):
    A cell is living if it is "on" in some way (like "█").

3. Dead (of a cell):
    A cell is dead if it is "off" in some way (like " ").

4. Generation (of a grid):
    A state of the grid at a certain point in time.

    For example, if the GOL rules haven't been applied yet, then the cell is said
    to be in the first generation.
    
    Every time that the rules are applied, a new
    generation (a new version or state of the grid) is created.

    The first time the rules are applied, the second generation is made.
    The second time the rules are applied, the third generation is made and so on.

5. Rule (of a cellular automaton):
    Explanatory, but a rule is something that is applied or is enforced in order
    to create a new generation for a grid.