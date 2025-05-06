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

if __name__ == '__main__':
    # Example run with a 5×5 board
    b = Board(size=5)
    print("Computer’s ships (for testing):")
    b.display(reveal=True)
    print("\nHidden view (player’s board):")
    b.display(reveal=False)
