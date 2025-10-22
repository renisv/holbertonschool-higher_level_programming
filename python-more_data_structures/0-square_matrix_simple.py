#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        row_squared = []
        for item in row:
            row_squared.append(item * item)
        squared_matrix.append(row_squared)
    return squared_matrix
