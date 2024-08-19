import pygame
from random import randint
import colors
import numpy as np

# game variables
game_started = False

# create matrix
matrix = np.zeros((20, 10), dtype=int)

# Initialize all Pygame modules
pygame.init()

# font setup
font = pygame.font.Font(None, 25)

# Create a window and
screen_width = 400
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python Tetris")

# Main game loop
running = True
while running:
    # fill in screen color
    screen.fill(colors.dark_python_grey)
    border = pygame.draw.rect(screen, colors.light_python_grey, (300, 0, 5, 800), )

    # check for events
    for event in pygame.event.get():
        # close window with mouse on X
        if event.type == pygame.QUIT:
            running = False
        # move falling object
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                game_started = True

            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                game_started = True

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                game_started = True

            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                game_started = True

    # display controls before game start
    if not game_started:
        starting_message = font.render(f"Press W,A,S,D or the arrow keys to start", True, colors.red)
        screen.blit(starting_message, (40, 400))

    # refresh screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
