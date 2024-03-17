"""
Tic Tac Toe Player
"""
import copy
import math

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
    Xs = 0
    Os = 0
    for row in board:
        for elem in row:
            if elem is X:
                Xs += 1
            if elem is O:
                Os += 1
    if Xs == 0 and Os == 0:
        return X
    if Xs > Os:
        return O
    elif Xs == Os:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    PossibleActions = set()

    for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] is EMPTY:
                    PossibleActions.add((i, j))

    return PossibleActions
    
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)
    if newBoard[action[0]][action[1]] in ['X', 'O']:
        raise ValueError('Este espaço ja possui uma jogada -_-')
    for i in range(len(board)):
        if i == action[0]:
            for j in range(len(board)):
                if j == action[1]:
                    newBoard[i][j] = player(newBoard)
                    break
    return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in (X, O):
            #verificar vertical
            for row in board:
                if row == [player] * 3:
                    return player
            #verificar vertical
            for i in range(3):
                column = [board[x][i] for x in range(3)]
                if column == [player] * 3:
                    return player
            #verificar diagonal
            if [board[i][i] for i in range(0, 3)] == [player] * 3:
                return player
            if [board[i][~i] for i in range(0, 3)] == [player] * 3:
                return player
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #se alguem vencer
    draw = 0
    is_draw = 0
    for c in range(len(board)):
        draw += len(board[c])
    if winner(board) in ['X', 'O']:
        return True
    #se empatar
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is not EMPTY:
                is_draw += 1
            if is_draw == draw:
                return True
    return False
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is X:
        return 1
    elif winner(board) is O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -5
            for action in actions(board):
                minval = min_value(result(board, action))[0]
                print(minval)
                if minval > v:
                    v = minval
                    optimal_move = action
            return v, optimal_move
    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = 5
            for action in actions(board):
                maxval = max_value(result(board, action))[0]
                if maxval < v:
                    v = maxval
                    optimal_move = action
            return v, optimal_move
    
    curr_player = player(board)

    if terminal(board):
        return None
    
    if curr_player == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]
