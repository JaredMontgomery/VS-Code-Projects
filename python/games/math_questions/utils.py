def safe_input(text: str, expected_type: type) -> object:
    """
    Summary:
        Takes input, but makes sure that it is of the right type before
        returning.

    Parameters:
        [text] - Prompt message to print out for the user.
        [expected_type] - The type that the input should be. Needs to be a
        class.
    """

    while True:
        try:
            return expected_type(input(text))
        # If conversion fails, then we repeat.
        except ValueError:
            pass