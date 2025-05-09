from battleships import Board

def main():
    enemy = Board(size=5)
    status, length = enemy.register_shot(0, 0)
    print(
        f"Shot at (0,0): {status}"
        + (f" (sunk size {length})" if status == "sunk" else "")
    )
    print("\nEnemy board (hidden):")
    enemy.display(reveal=False)

if __name__ == "__main__":
    main()
