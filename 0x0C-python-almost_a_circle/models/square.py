#!/usr/bin/python3
""" Defines a class called Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class representing a square shape, inherits from Rectangle.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The unique identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object with specified size, x, y, and id.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate
            of the square's position. Defaults to 0.
            y (int, optional): The y-coordinate
            of the square's position. Defaults to 0.
            id (int, optional): The unique identifier
            of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: A string representation of the Square object.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
