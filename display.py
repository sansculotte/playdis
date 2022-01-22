from __future__ import print_function
import pygame
import sys
from glob import glob


xs = glob('jesus/*.jpg')

if not xs:
    print('no images found')
    sys.exit()

i = 0
images = [pygame.image.load(x) for x in xs]

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                i = i - 1 if i > 0 else len(xs) - 1
            if event.key == pygame.K_RIGHT:
                i = i + 1 if i < len(xs) else 0
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(images[i], (0, 0))
    pygame.display.update()
