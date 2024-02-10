#!/usr/bin/python3
"""Defines a base model class """


class Base:
    """Base class for managing ID attributes in future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance with an ID.

        Args:
            id (int, optional): The ID to assign to the instance.
            If None,a new ID will be generated based on the number
            of objects created so far.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
