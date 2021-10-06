#!/usr/bin/python3

"""function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """
    Divides the elements of the matrix by
    means of div, in case of error it is
    because the elements are not valid
    otherwise it returns the matrix with
    its divided elements.
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix " +
                        "(list of lists) of integers/floats")
    x = 0
    for j in matrix:
        for i in j:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")

        if x == 0:
            x = len(j)
        elif x != len(j):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(n / div, 2) for n in j] for j in matrix]
