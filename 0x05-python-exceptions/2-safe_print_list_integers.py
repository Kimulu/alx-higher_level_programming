#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                num_printed += 1
        print()  # Add a newline after printing all integers
    except IndexError:
        print("list index out of range")

    return num_printed
