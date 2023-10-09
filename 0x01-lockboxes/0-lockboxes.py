#!/usr/bin/python3
""" module to check lockboxes
"""


def canUnlockAll(boxes):
    """ boxes -> list of lists, each box (list) with key(s) to next box(es)
        return True if all boxes can be unlocked else False
    """
    keys = list()
    keys.append(0)  # first box is always open
    for idx, r in enumerate(boxes):
        if idx not in keys:  # box not opened
            return False
        for el in r:
            if el not in keys and el < len(boxes) and el != 0:
                # key should be < num of boxes, first box open
                keys.append(el)
                # for each key, unlock the boxes to access next
                for k in boxes[el]:
                    if k not in keys and k < len(boxes) and k != 0:
                        keys.append(k)
    return True
