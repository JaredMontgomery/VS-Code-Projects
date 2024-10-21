def rect(width: int, height: int, void_char: str = " ", outline_char: str = "#") -> list:
    """
    Draws a rectangle of a certain size with a certain char ([outline_char]). The
    inside is filled with [void_char].

    Time complexity - O(N * M), where N is [width] and M is [height].
    Space complexity - O(N * M).
    """

    # Non-positive dimensions result in no shape.
    if width <= 0:
        raise ValueError(f"width ({width}) must be positive.")
    elif height <= 0:
        raise ValueError(f"height ({height}) must be positive.")
    
    # Holds each row of the rectangle.
    rect_strs: list = []
    
    # Adds each row.
    for i in range(height):
        rect_strs += [[void_char] * width]

    # Draws top side.
    for x in range(0, width - 1):
        rect_strs[0][x] = outline_char

    # Draws right side.
    for y in range(0, height - 1):
        rect_strs[y][-1] = outline_char
    
    # Draws bottom side.
    for x in range(width - 1, 0, -1):
        rect_strs[-1][x] = outline_char
    
    # Draws left side.
    for y in range(height - 1, 0, -1):
        rect_strs[y][0] = outline_char
    
    # Converts all row lists to strings and concats the strings with newlines.
    return "".join(["".join(row) + "\n" for row in rect_strs])