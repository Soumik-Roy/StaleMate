from chesswar import Board
from player_models import *
from score_heuristics import *
import curses
from curses import wrapper

# create an chesswar board (by default 7x7)
player1 = AlphaBetaPlayer()
player2 = AlphaBetaPlayer()
game = Board(player1, player2, player_1_piece='queen', player_2_piece='queen')

# place player 1 on the board at row 2, column 3, then place player 2 on
# the board at row 0, column 5; display the resulting board state.  Note
# that the .apply_move() method changes the calling object in-place.
game.apply_move((0, 0))
game.apply_move((3, 3))
print(game.to_string())

# players take turns moving on the board, so player1 should be next to move
assert(player1 == game.active_player)

# get a list of the legal moves available to the active player
print('Legal moves for player 1: {}'.format(game.get_legal_moves()))

# # get a successor of the current state by making a copy of the board and
# # applying a move. Notice that this does NOT change the calling object
# # (unlike .apply_move()).
# new_game = game.forecast_move((1, 1))
# assert(new_game.to_string() != game.to_string())
# print("\nOld state:\n{}".format(game.to_string()))
# print("\nNew state:\n{}".format(new_game.to_string()))

# play the remainder of the game automatically -- outcome can be "illegal
# move", "timeout", or "forfeit"
winner, history, outcome = game.play()
print("\nWinner: {}\nOutcome: {}".format('Player1' if (winner==player1) else 'Player2', outcome))
print(game.to_string())
print("Move history:\n{!s}".format(history))
