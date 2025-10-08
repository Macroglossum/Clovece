import pygame
from GUI import draw_resizable_circle

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Člověče, nezlob se!")

circle_img = pygame.image.load("Temple/circle_base.png").convert_alpha()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
        if event.type == pygame.QUIT:
            running = False

    draw_resizable_circle(screen, circle_img)
    pygame.display.flip()

pygame.quit()