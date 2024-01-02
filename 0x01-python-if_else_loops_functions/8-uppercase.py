#!/usr/bin/python3
def uppercase(input_str):
    output_str = ""

    for char in input_str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            output_str += uppercase_char
        else:
            output_str += char

    print("{}".format(output_str))
