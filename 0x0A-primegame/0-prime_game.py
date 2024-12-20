#!/usr/bin/python3
"""
find winner of prime game
"""


def isWinner(x, nums):
    """
    Maria or Ben
    """
    if x is None or nums == [] or x == 0 or nums is None:
        return None

    def primes(n):
        """
        Return all primes up to n
        """
        sieve = [True] * (n + 1)
        res = 0
        for x in range(2, n + 1):
            if sieve[x]:
                res += 1
                for i in range(x*x, n + 1, x):
                    sieve[i] = False
        return res

    Ben = 0
    Maria = 0
    for i in range(x):
        if primes(nums[i]) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Ben > Maria:
        return "Ben"
    elif Ben < Maria:
        return "Maria"
    else:
        return None
