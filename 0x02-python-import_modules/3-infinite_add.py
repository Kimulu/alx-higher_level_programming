#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    total = sum(int(j) for j in arguments)
    print(total)
