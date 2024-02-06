#!/usr/bin/python3
""" Represents a student with first name, last name, and age."""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first name,
        last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of strings containing attribute names. 
            Only attributes with names in this list will be retrieved.
            If None, all attributes will be retrieved. Defaults to None.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            # If attrs is None, retrieve all attributes
            return self.__dict__
        else:
            # Initialize an empty dictionary to store selected attributes
            selected_attrs = {}
            # Iterate over the attribute names in attrs
            for attr_name in attrs:
                # Check if the attribute exists in the instance
                if hasattr(self, attr_name):
                    # Add the attribute to the selected_attrs dictionary
                    selected_attrs[attr_name] = getattr(self, attr_name)
            return selected_attrs

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a dictionary representation.

        Args:
            json (dict): A dictionary containing attribute names and their corresponding values.
        """
        # Update instance attributes based on the provided dictionary
        for attr_name, attr_value in json.items():
            setattr(self, attr_name, attr_value)
