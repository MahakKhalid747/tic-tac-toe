
import tools.display as dsp   # alias import
from game.board import Board  # from‑module import
from game.players import Player
from tools.logger import Logger  # from‑module import

"""
Control the overall game flow:
 - Prompt for player names
 - Show welcome message
 - Loop: display board, announce turn, get move, place marker, log, check win/draw
 - At end: announce result, ask to play again
"""

def main():
    
    #initialize display and logger
    display = dsp.Display()
    logger = Logger()

    #prompt for player names
    p1_name = input("Please enter Player 1 name: ").strip() or "Player 1"
    p2_name = input("Please enter Player 2 name: ").strip() or "Computer"

    #create player objects with markers X and O
    player1 = Player(p1_name, "X")
    player2 = Player(p2_name, "O")
    players = [player1, player2]

    #show welcome message
    display.welcome(p1_name, p2_name)

    #set up board and turn generator
    board = Board()
    turn_gen = board.turn_generator(players)

    #main game loop
    while True:
        # 1) display the current board
        display.show_board(board.board)

        # 2) determine current player and announce turn
        current_player = next(turn_gen)
        display.turn_message(current_player.name, current_player.marker)

        # 3) get move (human via display.ask_move, computer via Player.get_move)
        if current_player.name.lower() == "computer":
            row, col = current_player.get_move(board.board)
            print(f"{current_player.name} chose position {row*3 + col + 1}")
        else:
            row, col = display.ask_move(current_player.name)

        # 4) attempt to place the marker
        if not board.place_marker(row, col, current_player.marker):
            display.invalid_move()
            continue

        # 5) log the move
        logger.log_move(current_player.name, row, col, board.board)

        # 6) check for a win
        if board.check_winner(current_player.marker):
            display.show_board(board.board)
            display.show_winner(current_player.name)
            logger.log_winner(current_player.name)
            break

        # 7) check for draw
        if board.is_full():
            display.show_board(board.board)
            display.show_draw()
            logger.log_draw()
            break

    # after game ends, ask to play again
    again = input("Would you like to play again? (yes/no): ").strip().lower()
    if again == "yes":
        print("\nStarting a new game...\n")
        main()
    else:
        print("\nThanks for playing!")

if __name__ == "__main__":
    main()
