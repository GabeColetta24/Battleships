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
4. **Install dependancies**: 
    ```bash
    pip install -r requirements.txt
5. **Run the game**: 
    ```bash
    python battleships.py

## How to Use

Once installed and your virtual environment is active:

1. **Start the game**:
    ```bash
    python battleships.py
2. **Understand the prompt**: the game displays your own board (ships revealed), then shows an enemy board before your shot.
3. **Enter your shot**: input two coordinates—row and column—each from 0 to 4, separated by a space (e.g. 1 3), where the first number is the row and the second is the column.
4. **View the result**: the CLI will indicate a hit, miss, or ship sunk, with appropriate color-coded markers.
5. **Computer's turn**: the AI will then take a shot and display your updated board.
6. Repeat until all ships on one side are sunk.
7. **Quit early**: press Ctrl+C to exit the game at any time.