# Rock-Paper-Scissors Game

This is a console-based Rock-Paper-Scissors minigame implemented in Python. The game allows players to compete against the computer by choosing one of three options: Rock, Paper, or Scissors. The game logic determines the winner based on the standard rules of the game.

## Project Structure

```
rock-paper-scissors/
├── src/
│   ├── game.py       # Main game execution file
│   ├── logic.py      # Game logic implementation
│   └── utils.py      # Utility functions for input handling
├── tests/
│   └── test_logic.py # Unit tests for the game logic
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
```

## How to Run the Game

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
4. Run the game by executing:
   ```
   python src/game.py
   ```

## Game Rules

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

Enjoy playing the game!