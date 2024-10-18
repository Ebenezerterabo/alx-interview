#!/usr/bin/python3


def sieve_of_eratosthenes(n):
    """ Returns a list of booleans where true indicates the number is prime """
    primes = [True] * (n + 1)  # List of booleans
    primes[0] = primes[1] = False  # 0 and 1 are not prime

    # Loop through numbers 2 to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:  # If the number is prime
            for j in range(i * i, n + 1, i):  # Loop through multiples of i
                primes[j] = False  # Mark multiples as non-prime

    return primes


def count_primes(n, primes):
    """ Returns the number of primes less than or equal to n """
    return sum(primes[:n + 1])


def isWinner(x, nums):
    """ Determines the winner of the prime game """
    if x == 0 or not nums:
        return None

    # Find the maximum n in nums
    max_n = max(nums)

    # Get the primes from the sieve of eratosthenes
    primes = sieve_of_eratosthenes(max_n)

    # Initialize win counters for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Simulate each round
    for n in nums:
        prime_count = count_primes(n, primes)

        # Determine the winner
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
