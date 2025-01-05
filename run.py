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

def make_shot(grid, x, y):
    """Processes a shot on the grid."""
    if grid[x][y] == "S":
        grid[x][y] = "X"
        print("Hit!")
        return True
    elif grid[x][y] == "~":
        grid[x][y] = "O"
        print("Miss.")
        return False
    else:
        print("You already shot here!")
        return False

def check_game_over(grid):
    """Checks if all ships have been sunk."""
    for row in grid:
        if "S" in row:
            return False
    return True

def battleships_game():
    """Main function for the Battleships game."""
    grid_size = 5
    ship_count = 3

    user_grid = initialize_grid(grid_size)
    computer_grid = initialize_grid(grid_size)

    place_ships(computer_grid, ship_count)

    print("Welcome to Battleships!")
    while True:
        print("Your grid:")
        print_grid(user_grid)

        print("Take your shot!")
        x, y = get_user_input()
        if 0 <= x < grid_size and 0 <= y < grid_size:
            make_shot(computer_grid, x, y)
            if check_game_over(computer_grid):
                print("Congratulations! You sank all the ships!")
                break
        else:
            print("Invalid coordinates. Please try again.")
        
        print("Opponent's turn to shoot.")
        while True:
            cx, cy = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
            if user_grid[cx][cy] in ["~", "S"]:
                hit = make_shot(user_grid, cx, cy)
                if hit and check_game_over(user_grid):
                    print("Game over! The opponent sank all your ships.")
                    return
                break

if __name__ == "__main__":
    battleships_game()