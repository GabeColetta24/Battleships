from battleships import Board

def main():
    # Smoke-test: instantiate a small board and verify ships were placed
    b = Board(size=3)
    assert len(b.ships) > 0

if __name__ == '__main__':
    main()
    print("✔️ Board smoke-test passed")
