#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Defines a square with a private instance attribute 'size'."""

    def __init__(self, size=0):
        """Instantiates a new Square.

        Args:
        - size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
