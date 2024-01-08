#!/usr/bin/env python3
def no_c(my_string):
    new = ""
    for char in my_string:
        if char.lower() not in {'c', 'C'}:
            new += char
    return new
