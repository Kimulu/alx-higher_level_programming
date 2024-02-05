#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""

class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        Args:
        name (str): The name of the parameter.
        value (int): The parameter to validate.
        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """
        Initializes a rectangle with a specified width and height.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def print(self):
        """Prints the rectangle description."""
        print(self.__str__())
