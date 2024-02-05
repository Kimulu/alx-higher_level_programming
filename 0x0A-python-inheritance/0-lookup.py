#!/usr/bin/python3

""" function that returns the list of available attributes and methods of an object"""


def lookup(obj):
    """
    Returns a list of non-hidden attributes and methods of an object.

    Parameters:
    - obj: The object for which attributes and methods are to be looked up.

    Returns:
    A list of attribute and method names.
    """
    # Get the list of all attributes and methods of the object
    all_attributes_and_methods = dir(obj)
    
    # Initialize an empty list to store filtered attributes and methods
    filtered_attributes_and_methods = []

    # Iterate through all attributes and methods
    for attr in all_attributes_and_methods:
        if not callable(getattr(obj, attr)) or not attr.startswith("__"):
            # Add the attribute or method to the filtered list
            filtered_attributes_and_methods.append(attr)

    return filtered_attributes_and_methods

