#!/usr/bin/python3
def islower(c):
    try:
        if len(c) > 0:
            # Check if the character is a lowercase letter
            return 'a' <= c <= 'z'
    except Exception as e:
        return f'Traceback: {str(e)}'
