def rect(width: int, height: int, voidChar: str = " ", outlineChar: str = "#", isFilled: bool = False, fillChar: str = "#") -> list:
    # Non-positive dimensions result in no shape.
    if width <= 0:
        raise ValueError(f"width ({width}) must be positive.")
    elif height <= 0:
        raise ValueError(f"height ({height}) must be positive.")
    
    # Holds each row of the rectangle.
    rectStrs: list = []
    
    # Adds each row.
    for i in range(height):
        rectStrs += [[voidChar] * width]

    # Draws top side.
    for x in range(0, width - 1):
        rectStrs[0][x] = outlineChar

    # Draws right side.
    for y in range(0, height - 1):
        rectStrs[y][-1] = outlineChar
    
    # Draws bottom side.
    for x in range(width - 1, 0, -1):
        rectStrs[-1][x] = outlineChar
    
    # Draws left side.
    for y in range(height - 1, 0, -1):
        rectStrs[y][0] = outlineChar
    
    # Converts all row lists to strings and concats the strings with newlines.
    return "".join(["".join(row) + "\n" for row in rectStrs])

print(rect(0, 10))