import random
import colorama
from colorama import Fore, Style

# Initialize colorama so colors reset after each print
colorama.init(autoreset=True)

class Board:
    """
    Represents a game board for Battleships, manages ship placement,
    tracking shots, and detecting hits, misses, and sunk ships.
    """
    # Cell states
    EMPTY = ' '   # no ship, no shot yet
    SHIP  = '■'   # a ship segment
    HIT   = 'X'   # ship was hit here
    MISS  = '·'   # shot into empty water

    def __init__(self, size=5, ship_sizes=None):
        """
        Initialize a size×size board and place ships.
        - size: grid dimension
        - ship_sizes: list of ship lengths to place
        """
        self.size = size
        # Default fleet: one length-3, two length-2, three length-1
        self.ship_sizes = ship_sizes or [3, 2, 2, 1, 1, 1]
        # Create an empty grid
        self.grid = [[self.EMPTY] * size for _ in range(size)]
        # Keep track of each ship's coordinates for sunk detection
        self.ships = []  # each ship is a list of (r,c) tuples
        # Randomly place all ships and record their positions
        self._place_all_ships()

    def _place_all_ships(self):
        """
        Place each ship in the fleet without overlapping.
        Records each ship's coordinate list in self.ships.
        """
        for length in self.ship_sizes:
            placed = False
            while not placed:
                orientation = random.choice(['H', 'V'])
                row = random.randrange(self.size)
                col = random.randrange(self.size)
                if self._can_place(row, col, length, orientation):
                    # Compute ship coordinates
                    dr, dc = (0, 1) if orientation == 'H' else (1, 0)
                    coords = [(row + dr * i, col + dc * i) for i in range(length)]
                    # Record the ship
                    self.ships.append(coords)
                    # Mark on grid
                    self._place_ship(row, col, length, orientation)
                    placed = True

    def _can_place(self, r, c, length, orientation):
        """
        Check if a ship of given length/orientation can go at (r,c)
        without going off-grid or overlapping another ship.
        """
        dr, dc = (0, 1) if orientation == 'H' else (1, 0)
        for i in range(length):
            rr, cc = r + dr * i, c + dc * i
            if not (0 <= rr < self.size and 0 <= cc < self.size):
                return False
            if self.grid[rr][cc] != self.EMPTY:
                return False
        return True

    def _place_ship(self, r, c, length, orientation):
        """Mark the cells for a ship of given length at (r,c)."""
        dr, dc = (0, 1) if orientation == 'H' else (1, 0)
        for i in range(length):
            self.grid[r + dr * i][c + dc * i] = self.SHIP

    def display(self, reveal=False):
        """
        Print the board with optional reveal of ships.
        - reveal=False: hides unhit ships (shows only hits/misses)
        - reveal=True: shows all ships
        """
        # Column headers
        header = '   ' + ' '.join(str(i) for i in range(self.size))
        print(header)
        # Each row
        for idx, row in enumerate(self.grid):
            row_str = []
            for cell in row:
                if cell == self.SHIP and not reveal:
                    display_char = self.EMPTY
                elif cell == self.HIT:
                    display_char = Fore.RED + cell + Style.RESET_ALL
                elif cell == self.MISS:
                    display_char = Fore.BLUE + cell + Style.RESET_ALL
                else:
                    display_char = cell
                row_str.append(display_char)
            print(f"{idx}  " + ' '.join(row_str))

    def register_shot(self, r, c):
        """
        Record a shot at (r,c).
        Returns a tuple (status, length):
        - status: 'invalid', 'miss', 'hit', or 'sunk'
        - length: length of sunk ship if status=='sunk', else None
        """
        # Validate coordinates
        if not (0 <= r < self.size and 0 <= c < self.size):
            return 'invalid', None
        cell = self.grid[r][c]
        # Already shot here?
        if cell in (self.HIT, self.MISS):
            return 'invalid', None
        # Hit
        if cell == self.SHIP:
            self.grid[r][c] = self.HIT
            # Identify which ship was hit
            for ship in self.ships:
                if (r, c) in ship:
                    # Check if all segments of this ship are hit
                    if all(self.grid[rr][cc] == self.HIT for rr, cc in ship):
                        # It's sunk!
                        self.ships.remove(ship)
                        return 'sunk', len(ship)
                    # Just a hit, not sunk yet
                    return 'hit', None
        # Miss
        if cell == self.EMPTY:
            self.grid[r][c] = self.MISS
            return 'miss', None
        # Fallback invalid
        return 'invalid', None


def play_game(size=5):
    """
    Orchestrate a full Battleships game:
    - size: dimension of the square grid
    """
    player_board = Board(size=size)
    computer_board = Board(size=size)

    print("Welcome to Battleships!")
    print("Your board (ships shown):")
    player_board.display(reveal=True)

    turn = 0  # 0 = player's turn, 1 = computer's turn
    while True:
        if turn == 0:
            # ---- Player's turn ----
            print("\nYour turn to shoot at the enemy.")
            while True:
                user_input = input("Enter row and column (e.g. `1 3`): ")
                try:
                    r_str, c_str = user_input.split()
                    r, c = int(r_str), int(c_str)
                except ValueError:
                    print("⚠️ Invalid format. Please enter two numbers separated by a space.")
                    continue

                status, length = computer_board.register_shot(r, c)
                if status == 'invalid':
                    print("⚠️ Off-grid or already shot. Try different coordinates.")
                    continue
                if status == 'hit':
                    print("✅ Hit!")
                elif status == 'sunk':
                    print(f"💥 You just sank an enemy ship of length {length}!")
                else:
                    print("❌ Miss.")
                break

            print("\nEnemy board:")
            computer_board.display(reveal=False)

            # Check for win
            if not computer_board.ships:
                print("\n🎉 You sank all the enemy ships! You win!")
                break

        else:
            # ---- Computer's turn ----
            print("\nComputer's turn to shoot at you...")
            while True:
                r = random.randrange(size)
                c = random.randrange(size)
                status, _ = player_board.register_shot(r, c)
                if status == 'invalid':
                    continue
                if status == 'hit':
                    print(f"Computer shot at ({r},{c}) and hit!")
                elif status == 'sunk':
                    print(f"Computer shot at ({r},{c}) and sunk one of your ships!")
                else:
                    print(f"Computer shot at ({r},{c}) and missed.")
                break

            print("\nYour board (ships & hits shown):")
            player_board.display(reveal=True)

            # Check for loss
            if not player_board.ships:
                print("\n💀 All your ships have been sunk. Game over.")
                break

        turn = 1 - turn


if __name__ == '__main__':
    play_game(size=5)
