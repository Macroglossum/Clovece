import pygame
import random
from GUI import draw_circle_grid

class GameInterface:
    def __init__(self, screen):
        self.screen = screen
        self.board_state = None
        self.figure_state = None
        self.base_images = {}
        self.figure_images = {}
        self.current_player = 2  # start with red
        self.dice_value = None

    def load_assets(self):
        self.base_images = {
            1: pygame.image.load("Temple/circle_base.png").convert_alpha(),
            2: pygame.image.load("Temple/circle_red.png").convert_alpha(),
            3: pygame.image.load("Temple/circle_blue.png").convert_alpha(),
            4: pygame.image.load("Temple/circle_green.png").convert_alpha(),
            5: pygame.image.load("Temple/circle_yellow.png").convert_alpha()
        }

        self.figure_images = {
            2: pygame.image.load("Temple/figure_red.png").convert_alpha(),
            3: pygame.image.load("Temple/figure_blue.png").convert_alpha(),
            4: pygame.image.load("Temple/figure_green.png").convert_alpha(),
            5: pygame.image.load("Temple/figure_yellow.png").convert_alpha()
        }

    def create_canvas(self):
        self.screen.fill((255, 255, 255))

    def set_board(self, board_mask, figure_map):
        self.board_state = board_mask
        self.figure_state = figure_map

    def draw_board(self):
        if self.board_state and self.figure_state:
            draw_circle_grid(self.screen, self.base_images, self.figure_images, self.board_state, self.figure_state)

    def roll_dice(self):
        self.dice_value = random.randint(1, 6)
        print(f"🎲 Player {self.current_player} rolled a {self.dice_value}")
        return self.dice_value

    def next_player(self):
        self.current_player = {2: 3, 3: 4, 4: 5, 5: 2}[self.current_player]

    def move_figure(self, from_pos, to_pos):
        r1, c1 = from_pos
        r2, c2 = to_pos
        fig = self.figure_state[r1][c1]
        self.figure_state[r1][c1] = 0
        self.figure_state[r2][c2] = fig