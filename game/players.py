''' create a Player class with attributes like 
name and marker (X or O). 
This class should include a method to prompt 
the player for input (or randomly select a move for 
computer players). '''

import random
from game.utils import clean_input, is_valid_move

class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def get_move(self, board):
        """
           If the player is a human, prompt for input.
           If the player is a computer, choose a random available move.
        """
        if self.name.lower() == "computer":
            # randomly select a move for computer players
            available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
            return random.choice(available_moves)
        else:
            # Prompt the human for a single position 1–9
            while True:
                pos_str = input(f"{self.name} ({self.marker}), enter a position (1-9): ")
                coords = clean_input(pos_str)
                if coords:
                    row, col = coords
                    if is_valid_move(board, row, col):
                        return row, col
                    else:
                        print("That cell is already taken. Try again.")
                else:
                    print("Invalid input. Enter a number from 1 to 9.")
