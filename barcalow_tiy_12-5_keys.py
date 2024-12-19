import sys

import pygame
from pygame.locals import *

screen = pygame.display.set_mode((200, 200))

pygame.font.init()

while True:
    screen.fill((200, 200, 200))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            print(event.key)

    pygame.display.update()
