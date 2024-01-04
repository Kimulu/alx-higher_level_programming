#!/usr/bin/python3
from sys import argv

def print_arguments():
    # Get the number of arguments
    num_arguments = len(argv) - 1  # Subtract 1 to exclude the script name

    # Print the number of arguments
    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
    else:
        print(f"{num_arguments} arguments:")

        # Print each argument with its position
        for i in range(1, num_arguments + 1):
            print(f"{i}: {argv[i]}")

# Call the function to print the arguments
if __name__ == "__main__":
    print_arguments()

