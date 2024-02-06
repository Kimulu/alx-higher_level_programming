#!/usr/bin/python3
""" Read the contents of a text file (UTF-8) and print it to stdout. """


def read_file(filename=""):
    """
    Read the contents of a text file (UTF-8) and print it to stdout.

    Args:
        filename (str, optional): The path to
        the text file to be read. Defaults to "".

    Returns:
        None
    """
    # Check if filename is provided
    if not filename:
        print("Please provide a filename.")
        return
    
    # Open the file and read its contents
    with open(filename, "r", encoding="utf-8") as file:
        # Read the contents of the file
        contents = file.read()
        # Print the contents to stdout
        print(contents)
