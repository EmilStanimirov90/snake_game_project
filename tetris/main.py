import sys
import pygame
from grid import Grid
from colors import Colors
from bricks import *

# game initialisation /start/
pygame.init()

# create game window
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetriz")

# game speed
game_speed_FPS = 5
clock = pygame.time.Clock()

# create grid
game_grid = Grid()

block = IBrick()

# console grid representation
game_grid.print_grid()

# game loop
while True:

    # game exit and loop end
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # fill in screen
    screen.fill(Colors.pale_blue)
    # Drawing
    game_grid.draw(screen)
    block.draw(screen)

    # refresh screen changes at certain fps
    pygame.display.update()
    clock.tick(game_speed_FPS)
