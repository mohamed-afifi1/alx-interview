#!/usr/bin/python3

def makeChange(coins, total):
    """
    make change of total from coins
    """
    db = [total + 1] * (total + 1)
    db[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if total - coin >= 0:
                db[i] = min(db[i], 1 + db[i - coin])
    if db[total] == total + 1:
        return -1
    return db[total]