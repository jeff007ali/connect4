import numpy as np
import pygame
import sys
import math

ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

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

def draw_board(board):
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (c*SQUARE_SIZE+SQUARE_SIZE//2, r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE//2), RADIUS)



board = create_board()
print(board)
running = True
turn = 0

pygame.init()

SQUARE_SIZE = 100
width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE
size = (width, height)

RADIUS = int(SQUARE_SIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            # We can make running variable as False to quit the game
            # running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

            posx = event.pos[0]
            col = posx // SQUARE_SIZE
            print(col)

            # Ask for Player 1 input
            if turn % 2 == 0:
                # posx = event.pos[0]
                # col = posx // SQUARE_SIZE
                piece = 1

            # Ask for Player 2 input
            else:
                piece = 2

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, piece)

                if winning_move(board, piece):
                    print("Player {} wins!!!".format(piece))
                    running = False

            turn += 1
            print(board)
