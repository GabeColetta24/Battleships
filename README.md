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