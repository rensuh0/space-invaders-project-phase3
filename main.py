import pygame
import os
import time
import random

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders 1")

# loading game images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

#PLAYER/USER SHIP
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

#LOADING LASERS
RED_LASERS = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASERS = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASERS = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASERS = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

#LOADING BACKGROUND
BG = pygame.image.load(os.path.join("assets", "background-black.png"))


def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    
    def redraw_window():
        WIN.blit(BG, 0, 0)
        pygame.display.update()


    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
main()