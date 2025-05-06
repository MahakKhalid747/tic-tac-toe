'''
In tools/display.py, 
manage all user interface elements,
 such as printing welcome messages,
 displaying the board in a clean format, 
 announcing winners, and prompting moves.
'''

from game.utils import clean_input

class Display:
    
    #printing welcome messages
    def welcome(self, p1_name, p2_name):
        print(f"\nWelcome, {p1_name} and {p2_name}!")
        # underline the greeting
        print("=" * (11 + len(p1_name) + len(p2_name)))

    # displaying the board in a clean format
    def show_board(self, board):
        print("\nBoard:")
        for i in range(3):
            # show numbers 1–9 for empty cells, marker otherwise
            row_display = []
            for j in range(3):
                cell = board[i][j]
                if cell == " ":
                    row_display.append(str(i*3 + j + 1))
                else:
                    row_display.append(cell)
            print(" | ".join(row_display))
            if i < 2:
                print("--+---+--")

    #prompting moves
    def ask_move(self, player_name):
        while True:
            pos_str = input(f"Enter a position (1-9): ")
            coords = clean_input(pos_str)
            if coords:
                return coords
            else:
                print("Invalid input. Please enter a number from 1 to 9.")

    def invalid_move(self):
        print("That cell is already taken. Try again.")

    #announcing winners,
    def show_winner(self, winner_name):
        print(f"\n Congratulations {winner_name}, you win! ")

    def show_draw(self):
        print("\n It's a draw!")

    #announcing whose turn it is
    def turn_message(self, player_name, marker):
        print(f"\n{player_name}'s Turn ({marker}):")
