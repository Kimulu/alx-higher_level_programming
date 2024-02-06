#!/usr/bin/python3
""" Append a string to the end of a text file (UTF-8)
and return the number of characters added. """


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF-8)
    and return the number of characters added.

    Args:
        filename (str): The path to the text file to which
        the string will be appended.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    # Check if filename is provided
    if not filename:
        print("Please provide a filename.")
        return 0

    # Open the file in append mode, creating it if it doesn't exist
    with open(filename, "a", encoding="utf-8") as file:
        # Write the text to the end of the file
        file.write(text)
        # Return the number of characters added
        return len(text)
