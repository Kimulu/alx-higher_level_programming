#!/usr/bin/python3

"""A class representing a base geometry."""


class BaseGeometry:
    """
    A class representing a base geometry.

    Public Methods:
    - area(self): Raises an Exception with the
    message 'area() is not implemented.'
    - integer_validator(self, name, value):
    Validates the value as an integer.

    Attributes:
    - name: A string representing the name of the value.
    - value: The value to be validated.
    """

    def area(self):
        """
        Raises an Exception indicating that
        the 'area()' method is not implemented.

        Raises:
        - Exception: 'area() is not implemented'
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates the value as an integer.

        Parameters:
        - name: A string representing the name of the value.
        - value: The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
