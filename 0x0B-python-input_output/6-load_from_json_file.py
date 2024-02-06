#!/usr/bin/python3
"""  Create an object from a JSON file """


import json

def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to be loaded.

    Returns:
        object: The Python object created from
        the JSON data in the file.
    """
    # Read the JSON data from the file
    with open(filename, "r") as file:
        json_data = file.read()

    # Deserialize the JSON data to a Python object
    obj = json.loads(json_data)
    return obj
