import sys
import pygame
import colors

# game initialisation /start/
pygame.init()

# create game window
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetriz")

# game speed
game_speed_FPS = 5
clock = pygame.time.Clock()

# game loop
while True:

    # game exit and loop end
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # refresh screen changes at certain fps
    pygame.display.update()
    clock.tick(game_speed_FPS)
