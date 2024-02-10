#!/usr/bin/python3
""" Base class for all the other classes"""
import json


class Base:
    """
    Base class representing the base of all other classes in the project.

    Attributes:
        __nb_objects (int): A private class attribute representing
        the number of objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object with a specified id.

        Args:
            id (int, optional): The id of the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances inheriting from Base.

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj
            in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of dictionaries from the JSON string representation.

        Args:
            json_string (str): A string representing a list of dictionaries
            in JSON format.

        Returns:
            list: The list of dictionaries represented by json_string.
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with all attributes already set using the
        provided dictionary.

        Args:
            **dictionary: A dictionary containing attribute names and values.

        Returns:
            Base: An instance with all attributes set based on the
            provided dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a file.

        Returns:
            list: A list of instances loaded from the file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                dicts = cls.from_json_string(json_data)
                return [cls.create(**d) for d in dicts]
        except FileNotFoundError:
            return []
