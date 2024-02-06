#!/usr/bin/python3


import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


"""  Adds all arguments to a Python list and
saves them to a file named "add_item.json"""


def main():
    """
    Adds all arguments to a Python list and
    saves them to a file named "add_item.json".

    If the file doesn’t exist, it will be created.
    The list is saved as a JSON representation.

    Args:
        None

    Returns:
        None
    """
    # Load existing items from the file if it exists
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    # Add arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(items, "add_item.json")

    print("Items added:", sys.argv[1:])

if __name__ == "__main__":
    main()
