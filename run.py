import random

def initialize_grid(size):
    """Creates an empty grid of the given size."""
    return [["~" for _ in range(size)] for _ in range(size)]

def print_grid(grid, reveal_ships=False):
    """Prints the grid. Optionally reveals ships."""
    for row in grid:
        print(" ".join(row))
    print()

def place_ships(grid, ship_count):
    """Randomly places ships on the grid."""
    size = len(grid)
    for _ in range(ship_count):
        while True:
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
            if grid[x][y] == "~":
                grid[x][y] = "S"
                break

def get_user_input():
    """Gets the user's shot input."""
    while True:
        try:
            coords = input("Enter your shot (row,col): ")
            x, y = map(int, coords.split(","))
            return x, y
        except ValueError:
            print("Invalid input. Please enter in the format row,col (e.g., 1,2).")