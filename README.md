# Tic-Tac-Toe
## Description
CS50’s [Introduction to Artificial Intelligence with Python](https://www.edx.org/learn/artificial-intelligence/harvard-university-cs50-s-introduction-to-artificial-intelligence-with-python) Project 0 - [Tic-tac-toe](https://cs50.harvard.edu/ai/2024/projects/0/tictactoe/)

## Project description
Using Minimax, implement an AI to play Tic-Tac-Toe optimally.

## git clone https://github.com/Ayrton-Machado/tictactoe

## How to run
[Python3](https://www.python.org/) is a requirement.  
- Install pygame with `pip install pygame`
- Run with `python runner.py` or `python3 runner.py`

## TODO

Complete the implementations of player, actions, result, winner, terminal, utility, and minimax.

- [X] The player function should take a board state as input, and return which player’s turn it is (either X or O).
    - [X] In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
    - [X] Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).

- [X] The actions function should return a set of all of the possible actions that can be taken on a given board.
    - [X] Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
    - [X] Possible moves are any cells on the board that do not already have an X or an O in them.
    - [X] Any return value is acceptable if a terminal board is provided as input.

- [X] The result function takes a board and an action as input, and should return a new board state, without modifying the original board.
    - [X] If action is not a valid action for the board, your program should raise an exception.
    - [X] The returned board state should be the board that would result from taking the original input board, and letting the player whose turn it is make their move at the cell indicated by the input action.
    - [X] Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation. This means that simply updating a cell in board itself is not a correct implementation of the result function. You’ll likely want to make a deep copy of the board first before making any changes.
    
- [X] The winner function should accept a board as input, and return the winner of the board if there is one.
    - [X] If the X player has won the game, your function should return X. If the O player has won the game, your function should return O.
    - [X] One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
    - [X] You may assume that there will be at most one winner (that is, no board will ever have both players with three-in-a-row, since that would be an invalid board state).
    - [X] If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function should return None.

- [X] The terminal function should accept a board as input, and return a boolean value indicating whether the game is over.
    - [X] If the game is over, either because someone has won the game or because all cells have been filled without anyone winning, the function should return True.
    - [X] Otherwise, the function should return False if the game is still in progress.

- [X] The utility function should accept a terminal board as input and output the utility of the board.
    - [X] If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.
    - [X] You may assume utility will only be called on a board if terminal(board) is True.

- [X] The minimax function should take a board as input, and return the optimal move for the player to move on that board.
    - [X] The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
    - [X] If the board is a terminal board, the minimax function should return None.
