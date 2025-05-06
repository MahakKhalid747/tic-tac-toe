'''
In game/utils.py, add functions for 
validating move positions, 
cleaning inputs, 
and creating generators
 that yield available moves dynamically. 
'''

#functions for validating input,
def is_valid_input(value):
    try:
        v = int(value)
        return 1 <= v <= 9
    except ValueError:
        return False

#function for cleaning inputs, 
def clean_input(move_str):
    try:
        pos = int(move_str.strip())
        if 1 <= pos <= 9:
            idx = pos - 1
            row, col = divmod(idx, 3)
            return row, col
    except ValueError:
        pass
    return None

#functions for validating move position,
def is_valid_move(board, row, col):
    return board[row][col] == " "

#creating generators that yield available moves dynamically. 
def available_moves_generator(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                yield (i, j)
