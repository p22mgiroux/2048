# Author: MOG 12/9/21

import random
import pygame
import sys
import copy

pygame.init()

board = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

starting = random.sample(range(16), 2)
board[starting[0] // 4][starting[0] % 4] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
board[starting[1] // 4][starting[1] % 4] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])

def move_right(board): 
    for d in range(12):
        if board[d % 4][3 - (d // 4)] == 0:
            board[d % 4][3 - (d // 4)] = board[d % 4][2 - (d // 4)]
            board[d % 4][2 - (d // 4)] = 0


def move_left(board):
    for a in range(12):
        if board[a % 4][a // 4] == 0:
            board[(a % 4)][a // 4] = board[(a % 4)][(a // 4) + 1]
            board[(a % 4)][(a // 4) + 1] = 0


def move_up(board):
    for w in range(12):
        if board[w // 4][w % 4] == 0:
            board[w // 4][w % 4] = board[(w // 4) + 1][w % 4]
            board[(w // 4) + 1][w % 4] = 0


def move_down(board):
    for s in range(12):
        if board[3 - (s // 4)][s % 4] == 0:
            board[3 - (s // 4)][s % 4] = board[2 - (s // 4)][s % 4]
            board[2 - (s // 4)][s % 4] = 0


def draw_rounded_square_tile(surface,color,width,height,screen_width):
    pygame.draw.circle(surface, color, (width, height), 4)
    pygame.draw.circle(surface, color, (width + ((screen_width - 50) // 4) - 22, height + ((screen_width - 50) // 4) - 22), 4)
    pygame.draw.circle(surface, color, (width, height + ((screen_width - 50) // 4) - 22), 4)
    pygame.draw.circle(surface, color, (width + ((screen_width - 50) // 4) - 22, height), 4)

    pygame.draw.rect(surface, color, (width - 4, height, 8, ((screen_width - 50) // 4) - 22))
    pygame.draw.rect(surface, color, (width, height - 4, ((screen_width - 50) // 4) - 22, 8))
    pygame.draw.rect(surface, color, (width + ((screen_width - 50) // 4) - 26, height, 8, ((screen_width - 50) // 4) - 22))
    pygame.draw.rect(surface, color, (width, height + ((screen_width - 50) // 4) - 26, ((screen_width - 50) // 4) - 22, 8))

    pygame.draw.rect(surface, (color), (width, height, ((screen_width - 50) // 4) - 22, ((screen_width - 50) // 4) - 22))
    

def display_tiles():
    for x in range(4):
        for y in range(4):
            if board[y][x] == 2:
                draw_rounded_square_tile(screen, (238, 228, 218),x * (width - 50) // 4 + (25 + 7 + 4),y * (width - 50) // 4 + (height - width + 25 + 7 + 4), width)
                pygame.display.flip()
            elif board[y][x] == 4:
                draw_rounded_square_tile(screen, (238, 225, 201),x * (width - 50) // 4 + (25 + 7 + 4),y * (width - 50) // 4 + (height - width + 25 + 7 + 4), width)
                pygame.display.flip()
            elif board[y][x] == 8:
                draw_rounded_square_tile(screen, (243, 178, 122),x * (width - 50) // 4 + (25 + 7 + 4),y * (width - 50) // 4 + (height - width + 25 + 7 + 4), width)
                pygame.display.flip()
            elif board[y][x] == 16:
                draw_rounded_square_tile(screen, (246, 150, 100),x * (width - 50) // 4 + (25 + 7 + 4),y * (width - 50) // 4 + (height - width + 25 + 7 + 4), width)
                pygame.display.flip()
            elif board[y][x] == 32:
                draw_rounded_square_tile(screen, (247, 126, 96),x * (width - 50) // 4 + (25 + 7 + 4),y * (width - 50) // 4 + (height - width + 25 + 7 + 4), width)
                pygame.display.flip()
            elif board[y][x] == 64:
                draw_rounded_square_tile(screen, (247, 95, 59),x * (width - 50) // 4 + (25 + 7 + 4),y * (width - 50) // 4 + (height - width + 25 + 7 + 4), width)
                pygame.display.flip()
            elif board[y][x] == 128:
                draw_rounded_square_tile(screen, (237, 208, 115),x * (width - 50) // 4 + (25 + 7 + 4),y * (width - 50) // 4 + (height - width + 25 + 7 + 4), width)
                pygame.display.flip()
            elif board[y][x] == 256:
                draw_rounded_square_tile(screen, (237, 204, 98),x * (width - 50) // 4 + (25 + 7 + 4),y * (width - 50) // 4 + (height - width + 25 + 7 + 4), width)
                pygame.display.flip()
            elif board[y][x] == 512:
                draw_rounded_square_tile(screen, (237, 201, 80),x * (width - 50) // 4 + (25 + 7 + 4),y * (width - 50) // 4 + (height - width + 25 + 7 + 4), width)
                pygame.display.flip()
            elif board[y][x] == 1024:
                draw_rounded_square_tile(screen, (237, 197, 63),x * (width - 50) // 4 + (25 + 7 + 4),y * (width - 50) // 4 + (height - width + 25 + 7 + 4), width)
                pygame.display.flip()
            elif board[y][x] == 2048:
                draw_rounded_square_tile(screen, (0, 0, 0),x * (width - 50) // 4 + (25 + 7 + 4),y * (width - 50) // 4 + (height - width + 25 + 7 + 4), width)
                pygame.display.flip()
                    

width = 139 * 4 + 50
height = 900
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("2048")

def bkg():
    screen.fill((250, 248, 239))

    circle_radius = 7
    pygame.draw.circle(screen, (187, 173, 160), (25, height - width + 25), circle_radius)
    pygame.draw.circle(screen, (187, 173, 160), (25, height - 25), circle_radius)
    pygame.draw.circle(screen, (187, 173, 160), (width - 25, height - width + 25), circle_radius)
    pygame.draw.circle(screen, (187, 173, 160), (width - 25, height - 25), circle_radius)

    pygame.draw.rect(screen, (187, 173, 160), (25 - circle_radius, height - width + 25, circle_radius * 2, height - (height - width) - 50))
    pygame.draw.rect(screen, (187, 173, 160), (25, height - 25 - circle_radius, width - 50, circle_radius * 2))
    pygame.draw.rect(screen, (187, 173, 160), (width - 25 - circle_radius, height - width + 25, circle_radius * 2, height - (height - width) - 50))
    pygame.draw.rect(screen, (187, 173, 160), (25, height - width + 25 - circle_radius, width - 50, circle_radius * 2))

    pygame.draw.rect(screen, (187, 173, 160), (25, height - width + 25, width - 50, width - 50))

    for x in range(4):
        for y in range(4):
            draw_rounded_square_tile(screen, (205, 193, 180), 25 + x * (width - 50) // 4 + circle_radius + 4, height - width + 25 + y * (width - 50) // 4 + circle_radius + 4, width)

bkg()
display_tiles()

running = True
while running:
    old_board = copy.deepcopy(board)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                move_right(board)
                move_right(board)
                move_right(board)
                move_right(board)

                for d in range(12):
                    if board[d % 4][3 - (d // 4)] == board[d % 4][2 - (d // 4)] and board[d % 4][3 - (d // 4)] != 0:
                        board[d % 4][3 - (d // 4)] *= 2
                        board[d % 4][2 - (d // 4)] = 0

                move_right(board)
                move_right(board)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_left(board)
                move_left(board)
                move_left(board)
                move_left(board)
        
                for a in range(12):
                    if board[a % 4][a // 4] == board[a % 4][(a // 4) + 1] and board[a % 4][a // 4] != 0:
                        board[(a % 4)][a // 4] *= 2
                        board[(a % 4)][(a // 4) + 1] = 0

                move_left(board)
                move_left(board)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                move_up(board)
                move_up(board)
                move_up(board)
                move_up(board)

                for w in range(12):
                    if board[w // 4][w % 4] == board [(w // 4) + 1][w % 4] and board[w // 4][w % 4] != 0:
                        board[w // 4][w % 4] *= 2
                        board[(w // 4) + 1][w % 4] = 0
        
                move_up(board)
                move_up(board)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move_down(board)
                move_down(board)
                move_down(board)
                move_down(board)

                for s in range(12):
                    if board[3 - (s // 4)][s % 4] == board[2 - (s // 4)][s % 4] and board[3 - (s // 4)][s % 4] != 0:
                        board[3 - (s // 4)][s % 4] *= 2
                        board[2 - (s // 4)][s % 4] = 0

                move_down(board)
                move_down(board)

    if board != old_board:
        empty_spaces = []
        for space in range(16):
            if board[space // 4][space % 4] == 0:
                empty_spaces.append(space)
        position = random.choice(empty_spaces)
        board[position // 4][position % 4] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])

        bkg()
        display_tiles()
    
    pygame.display.flip()

pygame.quit()