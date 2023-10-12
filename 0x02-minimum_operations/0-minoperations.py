#!/usr/bin/python3
""" module with minOperations """


def minOperations(n):
    """ Find minimum operations to copy & paste xters
        to match n 'H' characters (initially only one 'H')
        Operations: Copy All, Paste

        Returns: minimum number of operations (int)
    """
    if not isinstance(n, int):
        return 0
    xters = 1  # only one xter at first
    copied = 0
    ops = 0
    while xters < n:
        if n % xters == 0:
            # copy all
            copied = xters
            ops += 1  # operation
            xters += copied  # paste the copied xters
            ops += 1
        elif n % copied == 0:
            xters += copied
            ops += 1
        else:
            ops = 0
            break
    return ops
