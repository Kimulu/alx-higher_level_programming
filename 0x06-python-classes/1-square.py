#!/usr/bin/python3

"""Create a class named Square to model and handle square shapes."""

class Square:
"""This class serves as a representation of a square."""

def __init__(self, size):
    """Instantiate a new Square object.

    Parameters:
    - size (int): The dimension of the square's sides.
    """
    self.__size = size
