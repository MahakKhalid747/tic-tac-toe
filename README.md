
# Tic-Tac-Toe (Command-Line Python Game)

A command-line Tic-Tac-Toe game using a structured modular Python project.

## How to Run

1. Make sure Python is installed.

2. Open your terminal or command prompt.

3. Navigate to the project folder: cd path\to\tic_tac_toe


4. Run the game: python main.py

## Concepts Used

- Classes and Objects (`Player`, `Board`, `Logger`)
- Generators (`turn_generator`, available moves)
- Directory management using `pathlib`
- Logging game history into auto-created folders
- Clean modular project structure

## Project Structure

tic_tac_toe/
├── main.py
├── game/
│ ├── board.py
│ ├── players.py
│ └── utils.py
├── tools/
│ ├── display.py
│ └── logger.py
├── game_log/ ← created automatically during gameplay
└── README.md