#!/usr/bin/python3
""" N queens problem """
from sys import argv


def is_safe(board, row, col):
    """ Check if it is safe to place a queen at board[row][col] """
    for r, c in enumerate(board):
        # Check if there's a conflict in the same column or diagonals
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def generate_board(n):
    """ Generate the board """
    results = [[]]  # Start with an empty list of results
    for queen in range(n):
        # Place each queen row by row, updating results each time
        results = solve_nqueens(queen, n, results)
    return results


def solve_nqueens(queen, n, prev_results):
    """ Solve the n queens problem """
    positions = []
    for result in prev_results:
        for col in range(n):
            # Only check if it's safe to place the queen
            if is_safe(result, queen, col):
                positions.append(result + [col])
    return positions


def main():
    """ Main function """
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    # Generate all valid board configurations
    results = generate_board(n)

    # Print results in the desired format
    for result in results:
        formatted_result = [[row, col] for row, col in enumerate(result)]
        print(formatted_result)


if __name__ == "__main__":
    main()
