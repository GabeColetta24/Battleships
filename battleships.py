import random

class Board:
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
        # Randomly place all ships
        self._place_all_ships()

    def _place_all_ships(self):
        """Place each ship in the fleet without overlapping."""
        for length in self.ship_sizes:
            placed = False
            while not placed:
                orientation = random.choice(['H', 'V'])
                row = random.randrange(self.size)
                col = random.randrange(self.size)
                if self._can_place(row, col, length, orientation):
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
        Print the board.
        - reveal=False: hides unhit ships (shows only hits/misses)
        - reveal=True: shows all ships
        """
        # Print column headers
        header = '   ' + ' '.join(str(i) for i in range(self.size))
        print(header)
        # Print each row with its index
        for idx, row in enumerate(self.grid):
            row_str = []
            for cell in row:
                if cell == self.SHIP and not reveal:
                    row_str.append(self.EMPTY)
                else:
                    row_str.append(cell)
            print(f"{idx}  " + ' '.join(row_str))

    def register_shot(self, r, c):
        """
        Record a shot at (r,c).
        - Returns True  for a hit
        - Returns False for a miss
        - Returns None  if invalid coords or already shot there
        """
        # Check bounds
        if not (0 <= r < self.size and 0 <= c < self.size):
            return None
        cell = self.grid[r][c]
        if cell == self.SHIP:
            self.grid[r][c] = self.HIT
            return True
        if cell == self.EMPTY:
            self.grid[r][c] = self.MISS
            return False
        # Already HIT or MISS
        return None

def play_game(size=5):
    """
    Orchestrate a full Battleships game:
    - size: dimension of the square grid
    """
    # 1) Create boards for player and computer
    player_board = Board(size=size)
    computer_board = Board(size=size)

    print("Welcome to Battleships!")
    print("Your board (ships shown):")
    player_board.display(reveal=True)

    turn = 0  # 0 = player’s turn, 1 = computer’s turn
    while True:
        if turn == 0:
            # ---- Player's turn ----
            print("\nYour turn to shoot at the enemy.")
            # Loop until valid, new coordinates are entered
            while True:
                user_input = input("Enter row and column (e.g. `1 3`): ")
                try:
                    r_str, c_str = user_input.split()
                    r, c = int(r_str), int(c_str)
                except ValueError:
                    print("⚠️ Invalid format. Please enter two numbers separated by a space.")
                    continue

                result = computer_board.register_shot(r, c)
                if result is None:
                    print("⚠️ Off-grid or already shot. Try different coordinates.")
                    continue
                print("✅ Hit!" if result else "❌ Miss.")
                break

            print("\nEnemy board:")
            computer_board.display(reveal=False)

            # Check for win
            if all(cell != Board.SHIP for row in computer_board.grid for cell in row):
                print("\n🎉 You sank all the enemy ships! You win!")
                break

        else:
            # ---- Computer's turn ----
            print("\nComputer's turn to shoot at you...")
            while True:
                r = random.randrange(size)
                c = random.randrange(size)
                result = player_board.register_shot(r, c)
                if result is None:
                    continue
                print(f"Computer shot at ({r},{c}) and {'hit!' if result else 'missed.'}")
                break

            print("\nYour board (ships & hits shown):")
            player_board.display(reveal=True)

            # Check for loss
            if all(cell != Board.SHIP for row in player_board.grid for cell in row):
                print("\n💀 All your ships have been sunk. Game over.")
                break

        # Switch turns
        turn = 1 - turn

if __name__ == '__main__':
    play_game(size=5)


