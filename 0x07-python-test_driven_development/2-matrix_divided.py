#!/usr/bin/python3'
""" function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ Definition of function that divides all elements of matrix

    Args:
        matrix (list of list of integers or float) argumet one:
        div (integer or float): argument two

    Raises:
        TypeError: if the content of the matrix is not float or int
        and if each row of the matrix not have the same size
        ZeroDivisionError: if div is zero

    Returns:
        a new matrix with it elements divides
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"

    for i in range(len(matrix)):
        for ii in range(len(matrix[i])):
            if type(matrix[i][ii]) not in [float, int]:
                raise TypeError(msg)
        if len(matrix[0]) is not len(matrix[i]):
            raise TypeError(msg2)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    m = matrix
    return list(map(lambda n: list(map(lambda y: round(y / div, 2), n)), m))
