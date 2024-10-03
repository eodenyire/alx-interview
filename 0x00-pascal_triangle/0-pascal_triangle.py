#!/usr/bin/python3
"""
Pascal's Triangle Generator
"""

def pascal_triangle(n):
    """Returns a list of integers representing Pascal’s triangle of n."""
    if n <= 0:
        return []  # Return an empty list if n is less than or equal to 0

    res = []
    for i in range(1, n + 1):
        level = []
        C = 1
        for j in range(1, i + 1):
            level.append(C)
            C = C * (i - j) // j
        res.append(level)

    return res
