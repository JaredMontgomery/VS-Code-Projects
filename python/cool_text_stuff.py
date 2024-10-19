def check_types(func, params: dict) -> None:
    """
    Summary:
        Checks to see if all passed arguments to a function have the right type.

        Time complexity - O(N), where N is the number of parameters that the
        function has.
        Space complexity - O(N).
    
    Parameters:
        [func] - The function to type-check.
        [params] - A dict containing parameter names and their values.
    """

    # Iterate over param names:
    for anno in func.__annotations__:
        if anno == "return":
            break
        
        # If a param's expected type doesn't match the actual type passed, then
        # give an error.
        if func.__annotations__[anno] != type(params[anno]):
            raise TypeError(f"{anno} param has type {func.__annotations__[anno]} and not {type(params[anno])}")

def rotate_str(text: str, amount: int) -> str:
    """
    Summary:
        Moves chars in [text] over by [amount] places.

        Examples:

        rotate_str("1234", -1) == "2341"
        rotate_str("1234", -2) == "3412"
        rotate_str("1234", 1) == "4123"
        rotate_str("1234", 2) == "3412"

        Time complexity - O(N), where N is [amount].
        Space complexity - O(N).

    Parameters:
        [text] - Text to rotate around.
        [amount] - If positive, then [text] moves to right. If negative, moves
        go left.
    
    Returns:
        The rotated text.
    """

    check_types(rotate_str, locals())

    index: int = -amount % len(text)

    return text[index:] + text[:index]

def type_out(text: str, wait: float) -> None:
    """
    Summary:
        Slowly types out a message.

        Time complexity - O(N), where N is [len(text)].
        Space complexity - O(N).
    
    Parameters:
        [text] - Text to slowly type out.
        [wait] - The amount of time in seconds between each char print.
    """

    check_types(type_out, locals())

    from sys import stdout
    from time import sleep

    for char in text:
        print(char, end="")
        # Needs to be done, because print() doesn't actually print until a '\n'
        # is encountered or you do this.
        stdout.flush()

        sleep(wait)

def wave(text: str, min_height: int, max_height: int, rows: int, wait: float, align_left: bool = True) -> None:
    """
    Summary:
        Prints out text that comes in waves.

        Time complexity - O(N * M), where N is [max_height] and M is [rows].
        Space complexity - O(N).
    
    Parameters:
        [text] - The message to print out.
        [min_height] - Min height in chars for the wave.
        [max_height] - Max height in chars for the wave.
        [rows] - Total number of wave rows to print.
        [wait] - Time in seconds between each row print.
        [align_left] - If True, the wave rises from the left.
    """

    check_types(wave, locals())

    if type(text) != str:
        raise TypeError(f"{text} is of type {type(text)} and not str.")
    
    if type(min_height):
        pass

    from time import sleep

    # Counts number of rows printed.
    row_count: int = 0

    while True:
        # Prints a wave going up.
        for i in range(min_height, max_height):
            if align_left:
                # Prints a wave on the left.
                print(text * i)
            else:
                # Prints a wave on the right by adding spaces and then the
                # chars.
                print(" " * (max_height - i) + text * i)

            row_count += 1

            if row_count == rows:
                return

            sleep(wait)
        
        # Prints a wave going down.
        for i in range(max_height, min_height, -1):
            if align_left:
                print(text * i)
            else:
                print(" " * (max_height - i) + text * i)

            row_count += 1

            if row_count == rows:
                return

            sleep(wait)