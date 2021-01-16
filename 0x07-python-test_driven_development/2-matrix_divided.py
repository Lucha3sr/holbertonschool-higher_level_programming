#!/usr/bin/python3

"""

Function that divides all elements of a matrix.

"""


def matrix_divided(matrix, div):

    """
    matrix must be a list of lists of integers or floats
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in range(0, len(matrix)):
        if len(matrix[0]) != len(matrix[row]):
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for position in range(len(matrix)):
        new_matrix.append([])
        for nbr in matrix[position]:
            new_matrix[position].append(round((nbr / div), 2))
    return new_matrix
