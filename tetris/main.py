import sys
import pygame
from colors import Colors
from game import Game
from tetris.grid import Grid

# game initialisation /start/
pygame.init()

# create game window
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetriz")

# game speed
game_speed_FPS = 60
clock = pygame.time.Clock()

# instantiate game class
game = Game()

# move blocks down independently of game loop
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# game loop
while True:

    # game exit and loop end
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                game.rotate()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                game.move_down()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                game.move_right()
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                game.move_left()
            game_started = True
        # move blocks down independently of game loop
        if event.type == GAME_UPDATE:
            game.move_down()

    # fill in screen
    screen.fill(Colors.pale_blue)
    game.draw(screen)

    # refresh screen changes at certain fps
    pygame.display.update()
    clock.tick(game_speed_FPS)
