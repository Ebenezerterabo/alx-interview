#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Island Perimeter"""
    perimeter = 0

    # Get the size of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Loop through the rows
    for i in range(rows):
        # Loop through the columns
        for j in range(cols):
            # Checking the land cell
            if grid[i][j] == 1:
                # add 4 to the perimeter (maximun 4 sides)
                perimeter += 4
                # Check if the cell has a neighboring land
                # cell and substract the shared side
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    # return the perimeter
    return perimeter
