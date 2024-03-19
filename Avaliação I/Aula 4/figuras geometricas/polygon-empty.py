import pygame
import sys

pygame.init()

window = pygame.display.set_mode((600, 500))

black = 0, 0, 0
blue = (0, 0, 255)
white = 255, 255, 255

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    window.fill(black)

    pygame.draw.polygon(window, blue, [(150, 350), (300, 100), (450, 350)], 2)

    pygame.display.flip()