#!/usr/bin/python3
"""
pascal triange
"""


def pascal_triangle(n):
    """
    Generate a Pascal's triangle of size n.

    Args:
    n (int): The size of the triangle.

    Returns:
    list: A list of lists representing the Pascal's triangle.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        triangle.append([])
        triangle[i].append(1)
        for j in range(1, i):
            triangle[i].append(triangle[i-1][j] + triangle[i-1][j-1])
        triangle[i].append(1)
    return triangle
