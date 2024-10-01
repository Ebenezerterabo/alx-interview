#!/usr/bin/python3


# Transpose the matrix
def transpose_2d_matrix(matrix):
    """Function that transposes a 2D matrix
    """
    for i in range(len(matrix)):
        # Swap rows and columns (+1 to skip the diagonal numbers)
        for j in range(i + 1, len(matrix)):
            # Swap the numbers using In-place operations
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# Reverse the rows
def reverse_2d_matrix(matrix):
    """Function that reverses the rows of a 2D matrix
    """
    for i in range(len(matrix)):
        # Reverse each row
        matrix[i].reverse()


def rotate_2d_matrix(matrix):
    """Function that rotates a 2D matrix 90 degrees
    """
    transpose_2d_matrix(matrix)
    reverse_2d_matrix(matrix)
