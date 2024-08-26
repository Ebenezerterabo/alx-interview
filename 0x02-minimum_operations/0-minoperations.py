#!/usr/bin/env python3
""" 0-minoperations """


def minOperations(n: int) -> int:
    """ returns the fewest number of operations needed """
    if n <= 1:  # base case
        return 0

    operations = 0  # variable to keep track of total number of operations
    factor = 2  # variable to keep track of current factor

    while n > 1:
        # divide n by factor until n is divisible by factor
        while n % factor == 0:
            operations += factor  # add factor to operations
            n //= factor  # divide n by factor
        factor += 1  # move to the next factor

    return operations  # return the total number of operations
