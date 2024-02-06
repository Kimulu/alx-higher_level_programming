#!/usr/bin/python3
""" Returns a dictionary description with simple data structure
for JSON serialization of an object."""


def class_to_json(obj):
    """
    Returns a dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object with
        serializable attributes.
    """
    # Initialize an empty dictionary to store the serialized attributes
    serialized_obj = {}

    # Get all attributes of the object
    attributes = vars(obj)

    # Iterate over each attribute
    for attr_name, attr_value in attributes.items():
        # Check if the attribute value is serializable
        if isinstance(attr_value, (list, dict, str, int, bool)):
            # Add the attribute to the serialized dictionary
            serialized_obj[attr_name] = attr_value

    return serialized_obj
