#!/usr/bin/python3
""" Function that  writes an object
to a text file using its JSON representation. """
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using its JSON representation.

    Args:
        my_obj: The object to be serialized and saved to the file.
        filename (str): The name of the file to which
        the JSON representation will be saved.
    """
    # Serialize the object to JSON string
    json_string = json.dumps(my_obj)

    # Write the JSON string to the file
    with open(filename, "w") as file:
        file.write(json_string)
