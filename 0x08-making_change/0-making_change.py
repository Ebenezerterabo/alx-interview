#!/usr/bin/python3
""" Making Change module """


def makeChange(coins, total):
    """ returns the fewest number of coins needed to meet total
        if total is 0 or less, return 0
        if total cannot be met by any combination of the
        coins, return -1
    """

    # Base case when total is 0
    if total == 0:
        return 0

    # Initialize dp array with 'Infinity' for all values except dp[0]
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over amounts from 1 to total
    for amount in range(1, total + 1):
        # Iterate over coins
        for coin in coins:
            # If coin is less than amount, update dp[amount]
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is 'Infinity', return -1
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
