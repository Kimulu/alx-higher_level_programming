#!/usr/bin/python3
"""function that prints a text with 2 new lines after each of these characters: ., ? and : """
def text_indentation(text):
    """
    Print the text with 2 new lines after each '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty string to store the formatted text
    formatted_text = ""

    # Iterate through each character in the input text
    for char in text:
        # Append the character to the formatted_text
        formatted_text += char

        # Check if the character is '.', '?', or ':'
        if char in ('.', '?', ':'):
            # Add 2 new lines after the character
            formatted_text += '\n\n'

    # Print the formatted text
    print(formatted_text.strip())
