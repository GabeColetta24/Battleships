# Battleships

## Overview

Welcome to **Battleships**, a terminal-based classic naval strategy game. You command a hidden fleet on a customizable grid and take turns with a simple AI opponent to call shots, track hits and misses, and sink all enemy ships before they destroy yours.

## Features

- **Adjustable grid size**: Default is 5×5, but you can configure it in the code.
- **Input validation**:
  - Detects off-grid coordinates
  - Prevents repeated shots
  - Provides friendly error messages and re-prompts
- **Rich feedback**:
  - Hits (`X`) displayed in red
  - Misses (`·`) displayed in blue
  - Notifications when individual ships are sunk
- **Simple AI opponent**: Computer fires at random unseen cells
- Browser-based terminal gameplay via Heroku deployment

## Technologies Used

- **Python 3.x** – language and runtime  
- **Colorama** – for colored terminal output  
- **GitHub Actions** – continuous integration and CLI validation  

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/GabeColetta24/Battleships.git
2. **Navigate to the project folder**: 
    ```bash
    cd Battleships
3. **Create and activate a virtual environment**: 
    ```bash
    python3 -m venv venv
    source venv/bin/activate
4. **Install dependencies**: 
    ```bash
    pip install -r requirements.txt
5. **Run the game**: 
    ```bash
    python3 run.py

## How to Use

Once installed and your virtual environment is active:

1. **Start the game**:
    ```bash
    python3 run.py
2. **Understand the prompt**: the game displays your own board (ships revealed), then shows an enemy board before your shot.
3. **Enter your shot**: input two coordinates (row and column) each from 0 to 4, separated by a space (e.g. 1 3), where the first number is the row and the second is the column.
4. **View the result**: the CLI will indicate a hit, miss, or ship sunk, with appropriate color-coded markers.
5. **Computer's turn**: the AI will then take a shot and display your updated board.
6. Repeat until all ships on one side are sunk.
7. **Quit early**: press Ctrl+C to exit the game at any time.

## Planning

I mapped out the game using a flowchart before coding

![Flowchart of game logic](assets/documentation/battleship-flowchart.png)

This flowchart provided a clear blueprint for implementation, ensuring that each step (ship placement, input validation, hit/miss handling, and win detection) was developed in a logical order. 

## Manual Testing

- **Off-grid input**  
  Enter `9 9` → ⚠️ Displays “Off-grid or already shot” error and re-prompts.

  ![Off-grid input example](assets/documentation/off-grid.png)

- **Repeat shot**  
  Enter the same coordinates twice (e.g. `1 1` then `1 1`) → ⚠️ Displays “already shot” error and re-prompts.

  ![Repeat shot example](assets/documentation/already-shot.png)

- **Invalid format (missing space)**  
  Enter `22` → ⚠️ Displays “Invalid format. Please enter two numbers separated by a space.” and re-prompts.

  ![Invalid format example](assets/documentation/invalid.png)

- **Hit**  
  Shoot a cell containing a ship → ✅ Displays “Hit!” and marks the cell in red.

  ![Hit example](assets/documentation/hit.png)

- **Miss**  
  Shoot an empty cell → ❌ Displays “Miss.” and marks the cell in blue.

  ![Miss example](assets/documentation/miss.png)

- **Sunk**  
  Hit the final segment of a ship → 💥 Displays “You just sank an enemy ship of length X!”

  ![Sunk example](assets/documentation/sink.png)

- **Win condition**  
  Sink all enemy ships → 🎉 Displays “You sank all the enemy ships! You win!”

  ![Win example](assets/documentation/win.png)

- **Loss condition**  
  Have all your ships sunk → 💀 Displays “All your ships have been sunk. Game over.”

  ![Loss example](assets/documentation/lose.png)

### Code Style & Linting

- The codebase passes flake8 with no significant issues, helping ensure readable and PEP8-compliant Python code.

### Bugs Found & Fixed

- **Test unpacking error**  
  In `tests/test_board.py`, unpacking a list of tuples with `(r, c), = b.ships` raised a `ValueError`. Updated to `r, c = b.ships[0][0]` to correctly index the single-coordinate ship.

- **CI hang**  
  The initial smoke-test invoked the interactive loop. Resolved by moving to a standalone pytest suite in CI.

- **Long line in error message**  
  A runtime print statement exceeded PEP8’s line-length limit. Wrapped the string literal across two lines inside a `print(...)` call.

- **Imports in `conftest.py`**  
  Consolidated the `sys.path` hack into `tests/conftest.py` and ensured each import is on its own line to satisfy flake8’s E402/E401 rules.


## Future Enhancements

- **Dynamic grid sizing at runtime**: Prompt the player to choose grid dimensions before starting the game.
- **Advanced AI opponent**: Implement a hunt/target algorithm for smarter computer moves.
- **Manual ship placement**: Allow players to position their ships manually with coordinate input.
- **Multiplayer mode**: Add local or networked two-player functionality.
- **Replay & statistics**: Track and display win/loss records and session stats.


## Deployment & CI

This project is deployed using **Heroku** and the **Code Institute Python Terminal Template**, which allows the command-line Battleships game to run inside a browser terminal.

### Heroku Deployment Steps

1. Create a new app on **Heroku**.
2. Connect the Heroku app to the GitHub repository.
3. Add the required **buildpacks** in the following order:
  ```text
  heroku/nodejs
  heroku/python
  ```
4. Add the following **config variable** in the Heroku settings: PORT = 8000
5. Deploy the **main branch**.

### Live Application

The deployed game can be played here:

https://battleships-gcoletta-f205116c7c9d.herokuapp.com/

Click **Run Program** to start the game inside the browser terminal.

### GitHub Pages

The project documentation (README) is also available via GitHub Pages:

https://GabeColetta24.github.io/Battleships/

### Continuous Integration

GitHub Actions is used to run automated tests and validation checks on each push.

![CI](https://github.com/GabeColetta24/Battleships/actions/workflows/python-app.yml/badge.svg)


## Acknowledgements

- [Colorama](https://pypi.org/project/colorama/) – for easy terminal coloring  
- [Black](https://github.com/psf/black) – for auto-formatting Python code  
- [flake8](https://flake8.pycqa.org/) – for linting and style checks  
- StackOverflow and the Python docs for various implementation tips
