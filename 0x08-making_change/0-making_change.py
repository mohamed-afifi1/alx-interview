#!/usr/bin/python3
"""
coin change problem
"""


def makeChange(coins, total):
    """
    make change of total from coins
    """
    if total <= 0:
        return 0
    db = [total + 1] * (total + 1)
    db[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                db[i] = min(db[i], 1 + db[i - coin])
    return db[total] if db[total] <= total else -1
