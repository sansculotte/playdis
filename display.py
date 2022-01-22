from __future__ import print_function
import pygame
import sys
from glob import glob


xs = glob('*.png')

if not xs:
    print('no images found')
    sys.exit()

i = 0
images = [pygame.image.load(x) for x in sorted(xs)]
number_of_images = len(images)

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

while 1:
    screen.fill((0, 0, 0))
    screen.blit(images[i], (0, 0))
    pygame.display.update()


    dt = clock.tick(25)
    if dt >= 1000 / 25:
        i = (i + 1) % number_of_images
