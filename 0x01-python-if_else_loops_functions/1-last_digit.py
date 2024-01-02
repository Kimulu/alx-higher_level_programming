#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    sign = '-' if number < 0 else ''  # Determine the sign of the number
    print(f"Last digit of {number} is {sign}{abs(last_digit)} and is less than 6 and not 0")

