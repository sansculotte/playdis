#!/usr/bin/env python
from __future__ import print_function
import argparse
import pygame
import sys
from glob import glob


def loop_image_sequence(screen, clock, images, number_of_images, fps):
    """
    Loop play images at the specified fps
    """
    i = 0
    while 1:
        for event in pygame.event.get():
            if event.key == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        screen.blit(images[i], (0, 0))
        pygame.display.update()

        clock.tick(fps)
        i = (i + 1) % number_of_images


def switch_image_sequence(screen, images, number_of_images):
    """
    Switch images for- and backward with the arrow keys
    """
    i = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    i = (i - 1) % number_of_images
                if event.key == pygame.K_RIGHT:
                    i = (i + 1) % number_of_images
                if event.key == pygame.QUIT:
                    return

        screen.fill((0, 0, 0))
        screen.blit(images[i], (0, 0))
        pygame.display.update()


def display_images(args, images, number_of_images):
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    if args.play:
        loop_image_sequence(screen, clock, images, number_of_images, args.fps)
    else:
        switch_image_sequence(screen, images, number_of_images)

    pygame.display.quit()
    pygame.quit()


def load_images(xs):
    images = [pygame.image.load(x) for x in sorted(xs)]
    return images, len(images)


def main(args):
    xs = glob(args.images)
    if not xs:
        print('no images found')
        sys.exit()

    images, number_of_images = load_images(xs)
    display_images(args, images, number_of_images)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(
        description='Display images on the framebuffer'
    )
    ap.add_argument('images',
                    help='image files to display. may contain glob characters')
    ap.add_argument('-f', '--fps', type=float, default=25)
    ap.add_argument('-p', '--play', action='store_true', help='play image sequence')
    args = ap.parse_args()
    main(args)
    sys.exit()
