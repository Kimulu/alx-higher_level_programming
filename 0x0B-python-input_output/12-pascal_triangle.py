#!/usr/bin/python3
""" Generate Pascal's triangle for n rows """


def pascal_triangle(n):
    """
    Generate Pascal's triangle for n rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the Pascal's triangle with the first row
    triangle = [[1]]

    # Generate subsequent rows of Pascal's triangle
    for i in range(1, n):
        row = [1]  # Start each row with 1
        # Calculate the values for the current row based on the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
