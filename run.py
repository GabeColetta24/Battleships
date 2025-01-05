import random

def initialize_grid(size):
    """Creates an empty grid of the given size."""
    return [["~" for _ in range(size)] for _ in range(size)]

def print_grid(grid, reveal_ships=False):
    """Prints the grid. Optionally reveals ships."""
    for row in grid:
        print(" ".join(row))
    print()
