'''
AI50 2023
Week 0: tictactoe.py

Complete the implementations of player, actions, result, winner, terminal, utility, and minimax.

The player function should take a board state as input, and return which player’s turn it is (either X or O).
In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).

The actions function should return a set of all of the possible actions that can be taken on a given board.
Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2)
and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
Possible moves are any cells on the board that do not already have an X or an O in them.
Any return value is acceptable if a terminal board is provided as input.

The result function takes a board and an action as input, and should return a new board state,
without modifying the original board. If action is not a valid action for the board, your program should raise an exception.
The returned board state should be the board that would result from taking the original input board
and letting the player whose turn it is make their move at the cell indicated by the input action.
Importantly, the original board should be left unmodified: since Minimax will ultimately require considering
many different board states during its computation.This means that simply updating a cell
in board itself is not a correct implementation of the result function.
You’ll likely want to make a deep copy of the board first before making any changes.

The winner function should accept a board as input, and return the winner of the board if there is one.
If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.
One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
You may assume that there will be at most one winner (that is, no board will ever
have both players with three-in-a-row, since that would be an invalid board state).
If there is no winner of the game (either because the game is in progress,
or because it ended in a tie), the function should return None.

The terminal function should accept a board as input, and return a boolean value indicating whether the game is over.
If the game is over, either because someone has won the game or because all cells
have been filled without anyone winning, the function should return True.
Otherwise, the function should return False if the game is still in progress.

The utility function should accept a terminal board as input and output the utility of the board.
If X has won the game, the utility is 1. If O has won the game, the utility is -1.
If the game has ended in a tie, the utility is 0.
You may assume utility will only be called on a board if terminal(board) is True.

The minimax function should take a board as input, and return the optimal move for the player to move on that board.
The move returned should be the optimal action (i, j) that is one of the allowable actions on the board.
If multiple moves are equally optimal, any of those moves is acceptable.
If the board is a terminal board, the minimax function should return None.
For all functions that accept a board as input, you may assume that it is a valid board
(namely, that it is a list that contains three rows, each with three values of either X, O, or EMPTY).
You should not modify the function declarations (the order or number of arguments to each function) provided.

Once all functions are implemented correctly, you should be able to run python runner.py
and play against your AI. And, since Tic-Tac-Toe is a tie given optimal play by both sides,
you should never be able to beat the AI (though if you don’t play optimally as well, it may beat you!)
'''

import math
import copy


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count the number of X's and O's on the board
    num_X = sum(row.count(X) for row in board)
    num_O = sum(row.count(O) for row in board)

    # Determine which player has the next turn based on the number of X's and O's
    if num_X <= num_O:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # create an empty set to hold possible moves
    possible_moves = set()

    # iterate over each row and column in the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            # if the cell is empty, add the move to the set
            if board[i][j] == None:
                possible_moves.add((i, j))

    # return the set of possible moves
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Check if action is a valid 2-tuple.
    if len(action) != 2:
        raise ValueError("Invalid action")

    # Get row and column indices from the action.
    i, j = action

    # Check if the row and column indices are valid (between 0 and 2).
    if i < 0 or i > 2 or j < 0 or j > 2:
        raise ValueError("Invalid action")

    # Check if the cell is empty.
    if board[i][j] != EMPTY:
        raise ValueError("Cell is already occupied")

    # Create a new copy of the board.
    new_board = [row[:] for row in board]

    # Put the player's symbol (X or O) in the specified cell.
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # iterate over each player (X, O) to check if they won
    for player in (X, O):

        # check vertically
        for row in board:
            if row == [player] * 3:  # if the row contains all the same player
                return player

        # check horizontally
        for i in range(3):
            column = [board[x][i] for x in range(3)]
            if column == [player] * 3:  # if the column contains all the same player
                return player

        # check diagonally
        # if the diagonal from top-left to bottom-right contains all the same player
        if [board[i][i] for i in range(0, 3)] == [player] * 3:
            return player

        # if the diagonal from top-right to bottom-left contains all the same player
        elif [board[i][~i] for i in range(0, 3)] == [player] * 3:
            return player

    # if no player has won, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there is a winner
    if winner(board) == X or winner(board) == O:
        return True

    # Check if there are no empty cells left on the board
    elif EMPTY not in board[0] and EMPTY not in board[1] and EMPTY not in board[2]:
        return True

    # If neither of the above conditions are met, the game is not over yet
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_player = winner(board)  # get the winning player, if any

    if win_player == X:  # if X won, return 1
        return 1
    elif win_player == O:  # if O won, return -1
        return -1
    else:  # if no winner, return 0
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # Check if game is over
    if terminal(board):
        return None

    # If current player is X
    if player(board) == X:
        best_score = -math.inf
        best_action = None

        # Check all possible actions and choose one with highest score
        for action in actions(board):
            score = min_value(result(board, action))

            if score > best_score:
                best_score = score
                best_action = action

        return best_action

    # If current player is O
    elif player(board) == O:
        best_score = math.inf
        best_action = None

        # Check all possible actions and choose one with lowest score
        for action in actions(board):
            score = max_value(result(board, action))

            if score < best_score:
                best_score = score
                best_action = action

        return best_action


def min_value(board):
    """
    Returns the minimum value out of all maximum values
    """

    # Check if game is over
    if terminal(board):
        return utility(board)

    # Iterate over the available actions and return the minimum out of all maximums
    best_score = math.inf
    for action in actions(board):
        score = max_value(result(board, action))
        best_score = min(best_score, score)

    return best_score


def max_value(board):
    """
    Returns the maximum value out of all minimum values
    """

    # Check if game is over
    if terminal(board):
        return utility(board)

    # Iterate over the available actions and return the maximum out of all minimums
    best_score = -math.inf
    for action in actions(board):
        score = min_value(result(board, action))
        best_score = max(best_score, score)

    return best_score
