#!/usr/bin/python3
""" function that prints My name is <first name> <last name> """
def say_my_name(first_name, last_name=""):
    """
    Print a formatted string with the first and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the formatted string
    print(f"My name is {first_name} {last_name}")
