import sys
import os

# Insert the project root (one level up from tests/) onto sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from battleships import Board

@pytest.fixture
def small_board():
    # A minimal 3×3 board with two 1-segment ships
    return Board(size=3, ship_sizes=[1, 1])

def test_board_initialization(small_board):
    # Board.grid exists and has correct dimensions
    assert len(small_board.grid) == 3
    assert all(len(row) == 3 for row in small_board.grid)
    # Two ships should be recorded
    assert len(small_board.ships) == 2

def test_register_shot_miss(small_board):
    # Find an empty cell and ensure it reports a miss
    for r in range(3):
        for c in range(3):
            if small_board.grid[r][c] == Board.EMPTY:
                status, length = small_board.register_shot(r, c)
                assert status == 'miss'
                assert length is None
                return
    pytest.skip("No empty cell found to test miss")

def test_register_shot_hit_and_sunk():
    # Single-segment ship forced at size=1
    b = Board(size=3, ship_sizes=[1])
    # The ship’s only coord
    (r, c), = b.ships
    status, length = b.register_shot(r, c)
    assert status == 'sunk'
    assert length == 1

def test_invalid_shots(small_board):
    # Out-of-bounds
    status, _ = small_board.register_shot(-1, 0)
    assert status == 'invalid'
    # Repeat shot
    # First, a valid miss
    for r in range(3):
        for c in range(3):
            if small_board.grid[r][c] == Board.EMPTY:
                small_board.register_shot(r, c)
                # Now repeat
                status2, _ = small_board.register_shot(r, c)
                assert status2 == 'invalid'
                return
    pytest.skip("No empty cell to test repeat shot")
