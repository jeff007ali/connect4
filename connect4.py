import numpy as np
import pygame
import sys

ROW_COUNT = 6
COLUMN_COUNT = 7

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0 ,0)
YELLOW = (255, 255, 0)

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
            if board[r][c] == 0:
                pygame.draw.circle(screen, BLACK, (c*SQUARE_SIZE+SQUARE_SIZE//2, r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE//2), RADIUS)
            elif board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c*SQUARE_SIZE+SQUARE_SIZE//2, r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE//2), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (c*SQUARE_SIZE+SQUARE_SIZE//2, r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE//2), RADIUS)

    pygame.display.update()



board = create_board()
print(board)
running = True
turn = 0

pygame.init()

SQUARE_SIZE = 80 # Change game over text size also
width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE
size = (width, height)

RADIUS = int(SQUARE_SIZE/2 - 5)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect4 by jeff007ali")
draw_board(board)

game_over_font = pygame.font.SysFont("monospace", 55)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            # We can make running variable as False to quit the game
            # running = False

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
            posx = event.pos[0]
            if turn % 2 == 0:
                pygame.draw.circle(screen, RED, (posx, SQUARE_SIZE//2), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, SQUARE_SIZE//2), RADIUS)
            pygame.display.update()


        if event.type == pygame.MOUSEBUTTONDOWN:
            # For sometimes remove moving ball from top when Player makes their move
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))

            posx = event.pos[0]
            col = posx // SQUARE_SIZE

            # For Player 1
            if turn % 2 == 0:
                piece = 1
                color = RED

            # For Player 2
            else:
                piece = 2
                color = YELLOW

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, piece)

                if winning_move(board, piece):
                    print("Player {} wins!!!".format(piece))
                    label = game_over_font.render("Player {} wins!!!".format(piece), 1, color)
                    screen.blit(label, (40, 10))
                    running = False

            turn += 1
            print(turn)
            print(board)
            draw_board(board)

            if running == False:
                pygame.time.wait(3000)
