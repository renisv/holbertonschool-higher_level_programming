#!/usr/bin/python3

"""module to construct pascals triangle"""


def pascal_triangle(n):
    """func to print pascals triangle"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        last_row = triangle[-1]
        new_row = [1]
        for j in range(len(last_row) - 1):
            new_row.append(last_row[j] + last_row[j + 1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
