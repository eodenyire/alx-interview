#!/usr/bin/python3
"""
Pascal's Triangle Generator
"""


def pascal_triangle(n):
    """
    Returns a list of integers representing Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    res = []
    for i in range(1, n + 1):
        level = []
        C = 1
        for j in range(1, i + 1):
            level.append(C)
            C = C * (i - j) // j
        res.append(level)

    return res
