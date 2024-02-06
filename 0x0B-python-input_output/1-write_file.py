#!/usr/bin/python3
""" Write a string to a text file (UTF-8) and
return the number of characters written. """


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and
    return the number of characters written.

    Args:
        filename (str): The path to the text file to be written.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    # Check if filename is provided
    if not filename:
        print("Please provide a filename.")
        return 0

    # Open the file in write mode, creating it if it doesn't exist
    with open(filename, "w", encoding="utf-8") as file:
        # Write the text to the file
        file.write(text)
        # Return the number of characters written
        return len(text)
