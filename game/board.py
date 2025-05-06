'''
define a Board class that manages the board state. 
It should provide: 
methods for displaying the board,
 placing moves, 
 checking for winners across rows, 
columns,
 diagonals, 
and checking for a draw when the board is full. 
'''
class Board:
    #3x3 empty board
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    #methods for displaying the board
    def display(self):
        print("\nCurrent Board:")
        for i in range(3):
            # show numbers 1–9 for empty cells, marker otherwise
            row_display = []
            for j in range(3):
                cell = self.board[i][j]
                if cell == " ":
                    row_display.append(str(i*3 + j + 1))
                else:
                    row_display.append(cell)
            print(" | ".join(row_display))
            if i < 2:
                print("-----------")

    #method for placing moves
    def place_marker(self, row, col, marker):
        if self.board[row][col] == " ": #empty spot
            self.board[row][col] = marker #placing marker
            return True
        return False

    #checking for a draw when the board is full
    def is_full(self):
        for row in self.board:
            if " " in row:
                return False
        return True
    
    #checking for winners across rows
    def check_winner(self, marker):
        b = self.board
        # Rows and columns
        for i in range(3):
            if all([b[i][j] == marker for j in range(3)]) or \
               all([b[j][i] == marker for j in range(3)]):
                return True
        # Diagonals
        if b[0][0] == b[1][1] == b[2][2] == marker or \
           b[0][2] == b[1][1] == b[2][0] == marker:
            return True
        return False

    #repeat the same thing for other player
    def turn_generator(self, players):
        while True:
            for player in players:
                yield player
