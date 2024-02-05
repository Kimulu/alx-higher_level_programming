#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square using Rectangle."""

    def __init__(self, size):
        """
        Initializes a new square.

        Parameters:
        - size (int): The size of the square.
        """
        self.integer_validator('size', size)
        super().__init__(size, size)

    def __str__(self):
        """Returns the square description."""
        return "[Rectangle] {}/{}".format(self._Rectangle__width,
        self._Rectangle__height)
