import pygame
import sys

pygame.init()

size = width, height = 320, 240

window = pygame.display.set_mode((600, 500))

black = 0, 0, 0
white = 255, 255, 255

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    window.fill(black)

    pygame.draw.circle(window, (255, 0, 0), (300, 300), 3)

    pygame.display.flip()