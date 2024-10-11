#!/usr/bin/python3
"""
checks whether all boxes are posible to unlocked
"""


def canUnlockAll(boxes):
    """
    checks whether all boxes are posible to unlocked
    """
    if boxes is None or len(boxes) == 0:
        return False
    visted = [False] * len(boxes)

    def dfs(box):
        """
        dfs function
        """
        visted[box] = True
        for neighbor in boxes[box]:
            if not visted[neighbor]:
                dfs(neighbor)
    dfs(0)
    for v in visted:
        if v is False:
            return False
    return True
