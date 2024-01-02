#!/usr/bin/python3
def print_last_digit(number):
    # Ensure the number is positive
    number = abs(number)

    # Get the last digit using modulo 10
    last_digit = abs(number) % 10

    # Print the last digit
    print(last_digit, end="")

    # Return the value of the last digit
    return last_digit
