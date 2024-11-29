#!/usr/bin/python3
"""
coin change problem
"""


def makeChange(coins, total):
    """
    Make change of total from coins using memoization
    """
    db = {}
    
    def helper(n):
        if n in db:
            return db[n]
        if n == 0:
            return 0
        if n < 0:
            return 0
        
        min_coins = n + 1
        for coin in coins:
            num_coins = helper(n - coin) + 1
            if num_coins < min_coins:
                min_coins = num_coins
        
        db[n] = min_coins
        return db[n]

    result = helper(total)
    return result if result != float('inf') else -1
