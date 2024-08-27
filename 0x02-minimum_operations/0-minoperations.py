#!/usr/bin/env python3
""" 0-minoperations """


def minOperations(n: int) -> int:
    """ 
    returns the fewest number of operations needed

    Args:
        n: number of characters

    Returns:
        number of operations

    - base case
    - variable to keep track of total number of operations
    - variable to keep track of current factor

    - divide n by factor until n is divisible by factor
    - add factor to operations
    - divide n by factor

    - return the total number of operations
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
