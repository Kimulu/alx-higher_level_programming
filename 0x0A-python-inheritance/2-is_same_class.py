#!/usr/bin/python3

"""True if the object is exactly an instance of the specified class """


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The class to check against.

    Returns:
    True if the object is an instance of the specified class.
    """
    return type(obj) == a_class
