#!/usr/bin/python3
""" Making changes
    Given a pile of coins of different values
    determine the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """ Generate changes needed to reach total

    Arg:
        coins ([List]): [List of Coins available]
        total ([int]): [total amount needed]
    """
    if total <= 0:
        return 0
    Chk = 0
    tmp = 0
    coins.sort(reverse=True)
    for i in coins:
        while Chk < total:
            Chk += i
            tmp += 1
        if Chk == total:
            return tmp
        Chk -= i
        tmp -= 1
    return -1
