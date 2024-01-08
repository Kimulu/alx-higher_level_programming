#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    z = type(my_list)
    if z == list:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
