#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row for the result matrix with squared values
        squared_row = [num ** 2 for num in row]
        # Append the squared row to the result matrix
        result_matrix.append(squared_row)

    return result_matrix
