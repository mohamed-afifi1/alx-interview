#!/usr/bin/python3
"""
find winner of prime game
"""


def isWinner(x, nums):
    """
    Maria or Ben
    """
    def primes(n):
        """
        Return all primes up to n
        """
        sieve = [True] * (n + 1)
        for x in range(2, int(n**0.5) + 1):
            if sieve[x]:
                for i in range(x*x, n + 1, x):
                    sieve[i] = False
        res = 0
        for p in range(n):
            if sieve[p]:
                res += p
        return res
    Ben = 0
    Maria = 0
    for i in nums:
        if primes(i) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Ben > Maria:
        return "Ben"
    elif Ben < Maria:
        return "Maria"
    else:
        return None
