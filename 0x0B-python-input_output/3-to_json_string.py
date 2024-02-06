#!/usr/bin/python3
""" Function that returns the JSON
representation of an object (string). """


import json

def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    # Serialize the object to JSON string
    json_string = json.dumps(my_obj)
    return json_string
