#!/usr/bin/python3
import sys

def print_arguments():
    # Get the number of arguments
    num_arguments = len(sys.argv) - 1

    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
        print("1: Hello")
    else:
        print("{} arguments:".format(count))
        for j in range(num_arguments):
            print("{}: {}".format(i + 1,sys.argv[j + 1]))

# Call the function to print the arguments
if __name__ == "__main__":
    print_arguments()
