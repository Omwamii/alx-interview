#!/usr/bin/python3
""" fn to generate pascal's triangle
"""
def pascal_triangle(n):
    """ return list of lists of pascal's triangle numbers
    """
    if n <= 0:
        return []
    res = list()
    for i in range(0, n):
        row = list()
        if i == 0:
            row.append(1)
            res.append(row)  # first element
        else:
            row.append(1)
            for index, el in enumerate(res[i - 1]):
                if index + 1 > len(res[i - 1]) - 1:
                    # out of range
                    row.append(1)  # enclosing 1
                else:
                    row.append(el + res[i - 1][index + 1])
            res.append(row)
    return res
