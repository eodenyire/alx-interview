#!/usr/bin/python3
"""
Pascal's Triangle Generator

This script defines a function to generate Pascal's Triangle up to n levels.
Pascal's Triangle is a triangular array of binomial coefficients where 
each number is the sum of the two directly above it.

Example:
    The first 5 levels of Pascal's Triangle are:
        [1]
        [1, 1]
        [1, 2, 1]
        [1, 3, 3, 1]
        [1, 4, 6, 4, 1]
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
