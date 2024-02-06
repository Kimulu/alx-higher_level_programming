#!/usr/bin/python3
""" Function that returns the Python
data structure represented by a JSON string """


import json

def from_json_string(my_str):
    """
    Return the Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        object: The Python data structure represented by
        the JSON string.
    """
    # Deserialize the JSON string to a Python object
    obj = json.loads(my_str)
    return obj
