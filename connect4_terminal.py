import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[0][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT - 1, -1, -1):
        if board[r][col] == 0:
            return r

def winning_move(board, piece):
    # TODO : write optimized code to replace this brute force solution

    # Check horizontal locations for win
    # [[0. 0. 0. 1. 1. 1. 1.]
    #  [0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0.]]
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    
    # Check vertical locations for win
    # [[0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0.]
    #  [1. 0. 0. 0. 0. 0. 0.]
    #  [1. 0. 0. 0. 0. 0. 0.]
    #  [1. 0. 0. 0. 0. 0. 0.]
    #  [1. 0. 0. 0. 0. 0. 0.]]
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals for win
    # [[0. 0. 0. 1. 0. 0. 0.]
    #  [0. 0. 1. 0. 0. 0. 0.]
    #  [0. 1. 0. 0. 0. 0. 0.]
    #  [1. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0.]]
    for r in range(ROW_COUNT - 3):
        for c in range(3, COLUMN_COUNT):
            if board[r][c] == piece and board[r+1][c-1] == piece and board[r+2][c-2] == piece and board[r+3][c-3] == piece:
                return True

    # Check negatively sloped diagonals for win
    # [[0. 0. 0. 1. 0. 0. 0.]
    #  [0. 0. 0. 0. 1. 0. 0.]
    #  [0. 0. 0. 0. 0. 1. 0.]
    #  [0. 0. 0. 0. 0. 0. 1.]
    #  [0. 0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0. 0.]]
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True


board = create_board()
print(board)
running = True
turn = 0

while running:
    # Ask for Player 1 input
    if turn % 2 == 0:
        selection = int(input("Player 1 make your selection (1-7): "))
        piece = 1

    # Ask for Player 2 input
    else:
        selection = int(input("Player 2 make your selection (1-7): "))
        piece = 2

    # Reduce column by 1 because column index start from "0" and Player's selection start from "1" 
    col = selection -1

    if is_valid_location(board, col):
        row = get_next_open_row(board, col)
        drop_piece(board, row, col, piece)

        if winning_move(board, piece):
            print("Player {} wins!!!".format(piece))
            running = False

    turn += 1
    print(board)
