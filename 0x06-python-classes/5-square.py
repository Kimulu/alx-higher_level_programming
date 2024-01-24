#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Defines a square with private instance attribute 'size'."""

    def __init__(self, size=0):
        """Instantiates a new Square.

        Args:
        - size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size  # Utilizing the property setter for validation

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size with validation.

        Args:
        - value (int): The new size to be set.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
