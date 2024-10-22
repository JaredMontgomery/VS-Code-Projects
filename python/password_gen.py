def password_gen(length: int, upper: bool = True, lower: bool = True, numbers: bool = True, symbols: bool = True) -> str:
    """
    Summary:
        Generates a password of a certain length with different options for the
        chars used.

        Time complexity - O(N), where N is [length].
        Space complexity - O(N).

    Parameters:
        [length] - The number of characters in the password.

        [upper] - Whether to include uppercase letters.
        [lower] - Whether to include lowercase letters.
        [digits] - Whether to include digits.
        [symbols] - Whether to include symbols.
    
    Returns:
        The aforementioned password.
    """

    from random import choice

    # All of the characters that a password could have.
    ascii_uppercase: str = "QWERTYUIOPASDFGHJKLZXCVBNM"
    ascii_lowercase: str = "qwertyuiopasdfghjklzxcvbnm"
    digits: str = "1234567890"
    symbols: str = "~`!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/"

    # Will holds all of the chars for the password. Doing this so that a new str
    # doesn't need to be made on each iteration, which would be slow.
    password_chars: list[str] = [' '] * length
    # Holds what kind of characters are enabled (what params are set to True).
    char_options: str = ""

    # Adds chars to use for making a password.
    for option in [
        [upper, ascii_uppercase],
        [lower, ascii_lowercase],
        [numbers, digits],
        [symbols, symbols]
    ]:
        # If True, then a certain set of chars will be added for use.
        if option[0]:
            char_options += option[1]

    # Adds every char to the password:
    for i in range(length):
        # Randomly picks what kind of char to put this time.        
        password_chars[i] = choice(char_options)
    
    # Creates and returns the password.
    return "".join(password_chars)

print(password_gen(64))