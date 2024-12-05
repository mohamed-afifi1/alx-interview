#!/usr/bin/python3
"""
island perimeter
"""


def island_perimeter(grid):
    """
    Return the perimeter of the island.
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the adjacent cells
                if i > 0 and grid[i-1][j] == 0:
                    perimeter += 1
                if j > 0 and grid[i][j-1] == 0:
                    perimeter += 1
                if i < rows - 1 and grid[i+1][j] == 0:
                    perimeter += 1
                if j < cols - 1 and grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter
