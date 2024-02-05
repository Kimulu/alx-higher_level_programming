#!/usr/bin/python3
"""Defines a Sub class Square inheriting a Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """
        Initializes a new square.

        Parameters:
        - size (int): The size of the square.
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
