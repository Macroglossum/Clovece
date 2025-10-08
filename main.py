import pygame
from Interface import GameInterface

# Multi-value board mask (base circles)
BOARD_MASK = [
    [5, 5, 0, 0, 1, 1, 3, 0, 0, 3, 3],
    [5, 5, 0, 0, 1, 3, 1, 0, 0, 3, 3],
    [0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0],
    [5, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1],
    [1, 5, 5, 5, 5, 0, 4, 4, 4, 4, 1],
    [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 4],
    [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0],
    [2, 2, 0, 0, 1, 2, 1, 0, 0, 4, 4],
    [2, 2, 0, 0, 2, 1, 1, 0, 0, 4, 4],
]

# Figure placement map (player tokens)
FIGURE_MAP = [
    [5, 5, 0, 0, 0, 0, 0, 0, 0, 3, 3],
    [5, 5, 0, 0, 5, 0, 0, 0, 0, 3, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
    [2, 2, 0, 0, 0, 0, 0, 0, 0, 4, 4],
    [2, 2, 0, 0, 0, 0, 0, 0, 0, 4, 4],
]

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Člověče, nezlob se!")

game = GameInterface(screen)
game.load_assets()
game.set_board(BOARD_MASK, FIGURE_MAP)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
        if event.type == pygame.QUIT:
            running = False

    game.create_canvas()
    game.draw_board()
    pygame.display.flip()

pygame.quit()

