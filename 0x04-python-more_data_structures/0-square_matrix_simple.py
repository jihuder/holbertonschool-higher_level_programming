#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for i in range(len(new_matrix)):
        new_matrix[i] = list(map(lambda x: x * x, new_matrix[i]))
    return new_matrix
