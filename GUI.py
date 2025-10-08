import pygame

def draw_resizable_circle(surface, image):
    
    window_width, window_height = surface.get_size()
    circle_size = min(window_width, window_height)

    scaled_img = pygame.transform.smoothscale(image, (circle_size, circle_size))

    x = (window_width - circle_size) // 2
    y = (window_height - circle_size) // 2

    surface.fill((255, 255, 255))  # white background
    surface.blit(scaled_img, (x, y))