import pygame

# Grid settings
BOARD_ROWS = 11
BOARD_COLS = 11
GAP = 12  # spacing between cells
MARGIN_X = 40  # horizontal margin
MARGIN_Y = 40  # vertical margin
FIGURE_HEIGHT_RATIO = 0.08  # 8% of screen height
FIGURE_ASPECT_RATIO = 0.66  # width = 66% of height
FIGURE_Y_OFFSET = 11  # pushed 5px higher than before

def draw_circle_grid(surface, base_images, figure_images, BOARD_MASK, FIGURE_MAP):
    window_width, window_height = surface.get_size()

    total_gap_x = GAP * (BOARD_COLS - 1)
    total_gap_y = GAP * (BOARD_ROWS - 1)

    available_width = window_width - total_gap_x - 2 * MARGIN_X
    available_height = window_height - total_gap_y - 2 * MARGIN_Y

    circle_size = int(min(available_width / BOARD_COLS, available_height / BOARD_ROWS))
    if circle_size < 1:
        return

    # Pre-scale base circle images
    scaled_base = {
        key: pygame.transform.smoothscale(img, (circle_size, circle_size))
        for key, img in base_images.items()
    }

    # Scale figures based on screen height
    fig_height = int(window_height * FIGURE_HEIGHT_RATIO)
    fig_width = int(fig_height * FIGURE_ASPECT_RATIO)

    scaled_figures = {
        key: pygame.transform.smoothscale(img, (fig_width, fig_height))
        for key, img in figure_images.items()
    }

    board_width = BOARD_COLS * circle_size + total_gap_x
    board_height = BOARD_ROWS * circle_size + total_gap_y
    offset_x = MARGIN_X + (window_width - board_width - 2 * MARGIN_X) // 2
    offset_y = MARGIN_Y + (window_height - board_height - 2 * MARGIN_Y) // 2

    surface.fill((255, 255, 255))

    # Draw base circles
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            cell = BOARD_MASK[row][col]
            if cell == 0:
                continue
            img = scaled_base.get(cell)
            if img:
                x = offset_x + col * (circle_size + GAP)
                y = offset_y + row * (circle_size + GAP)
                surface.blit(img, (x, y))

    # Draw center square image (same size as one circle)
    square = pygame.image.load("Temple/kostka_1.png").convert_alpha()
    center_img = pygame.transform.smoothscale(square, (circle_size, circle_size))
    center_x = (window_width - circle_size) // 2
    center_y = (window_height - circle_size) // 2
    surface.blit(center_img, (center_x, center_y))

    # Draw figures
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            fig = FIGURE_MAP[row][col]
            if fig == 0:
                continue
            img = scaled_figures.get(fig)
            if img:
                x = offset_x + col * (circle_size + GAP) + (circle_size - fig_width) // 2
                y = offset_y + row * (circle_size + GAP) + (circle_size - fig_height) // 2 - FIGURE_Y_OFFSET
                surface.blit(img, (x, y))