'''
In tools/logger.py, create a Logger class responsible 
    for managing the game logs: 
• When a game starts, create a folder like 
    tic_tac_toe/game_log/game1/ using pathlib. 
• Create a text file log.txt in that folder. 
• After every move, log the move with move number, player name, and board position 
selected. 
• Also, include the board's visual state after each move. 
• After the game ends, log the final result (Win or Draw). 
Each new game must automatically create a new folder like game2/, game3/, etc., inside 
game_log/, without overwriting previous game logs. 
'''

from pathlib import Path
from datetime import datetime

class Logger:
    def __init__(self):
        # Create game_log directory
        base_log_path = Path(__file__).parent.parent / "game_log"
        base_log_path.mkdir(parents=True, exist_ok=True)

        # Determine next game number
        existing_games = [
            d for d in base_log_path.iterdir() 
            if d.is_dir() and d.name.startswith("game")
        ]
        game_number = len(existing_games) + 1
        self.game_dir = base_log_path / f"game{game_number}"
        self.game_dir.mkdir()

        # Create log file
        self.file = self.game_dir / "log.txt"
        self.move_count = 0
        self.file.write_text(f"Tic-Tac-Toe Game {game_number} started at {datetime.now()}\n\n")

    #log move in file and board state
    def log_move(self, player, row, col, board):
        self.move_count += 1
        with self.file.open("a") as f:
            f.write(f"Move {self.move_count}: {player} placed at ({row}, {col})\n")
            f.write("Board state:\n")
            for r in board:
                f.write(" | ".join(r) + "\n")
            f.write("-" * 9 + "\n")

    #log final result
    def log_winner(self, winner):
        with self.file.open("a") as f:
            f.write(f"\n {winner} won the game!\n")

    #log final result
    def log_draw(self):
        with self.file.open("a") as f:
            f.write("\n Game ended in a draw.\n")
