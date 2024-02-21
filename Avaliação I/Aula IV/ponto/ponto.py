import pygame
import sys

pygame.init()

window = pygame.display.set_mode((800, 500))

black = 0, 0, 0
white = 255, 255, 255

eixo_x = 300
eixo_y = 300

velocidade = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    window.fill(white)

    pygame.draw.circle(window, (0, 0, 255), (eixo_x, eixo_y), 6)

    eixo_x += velocidade

    if eixo_x >= 600:
        velocidade = 0

    pygame.display.flip()
    pygame.time.delay(10)
