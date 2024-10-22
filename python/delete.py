def delete(char_count: int) -> None:
    """
    Summary:
        If left running long enough, it will completely wipe all free space on
        a computer by writing random data. This can be used to truly delete any
        file.

        Time complexity - O(N), where N is [char_count].
        Space complexity - O(N).
    
    Parameters:
        [char_count] - The number of characters to write to memory.
    """

    from random import choice
    from string import printable

    # Opens a file and keeps writing junk to it.
    with open("file.txt", "w") as file:
        for i in range(char_count):
            file.write(choice(printable))