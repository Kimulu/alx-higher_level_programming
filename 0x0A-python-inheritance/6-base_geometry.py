#!/usr/bin/python3

"""A class representing a base geometry."""


class BaseGeometry:
    """
    A class representing a base geometry.

    Public Methods:
    - area(self): Raises an Exception with the
    message 'area() is not implemented.'
    """

    def area(self):
        """
        Raises an Exception indicating that
        the 'area()' method is not implemented.

        Raises:
        - Exception: 'area() is not implemented'
        """
        raise Exception('area() is not implemented')
