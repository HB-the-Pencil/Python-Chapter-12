import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1200, 700))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((100, 220, 255))

    pygame.display.flip()