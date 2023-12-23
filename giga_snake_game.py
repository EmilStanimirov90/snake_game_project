import pygame
from random import randint


def generate_food_at_random_position(scr):
    x = randint(0, 800)  # Replace 800 with your desired maximum x-coordinate
    y = randint(0, 800)  # Replace 800 with your desired maximum y-coordinate
    pink = (240, 60, 123)
    food = pygame.draw.circle(scr, pink, (x, y), 10)
    return food


pygame.init()

# create screen and name
game_board_x = 800
game_board_y = 800
game_board = pygame.display.set_mode((game_board_x, game_board_y))
pygame.display.set_caption("Giga-Mecha-Snake")

clock = pygame.time.Clock()

generate_food_at_random_position(game_board)

#game variables
cell_size = 20
direction = 1 # 1 is up 2 is down 3 is right 4 is left

# create snake
snake_position = [[int(game_board_x / 2), int(game_board_y / 2)],
                  [int(game_board_x / 2), int(game_board_y / 2) + cell_size],
                  [int(game_board_x / 2), int(game_board_y / 2) + cell_size * 2],
                  [int(game_board_x / 2), int(game_board_y / 2) + cell_size * 3],
                  [int(game_board_x / 2), int(game_board_y / 2) + cell_size * 4]
                  ]
# player_image = pygame.image.load('head.png')  # Load the player image
# snake_head_rect = player_image.get_rect()  # Get the rectangle that encloses the image
# snake_head_rect.center = (snake_position[0])


# define colors
orange = (206, 119, 50)
green = (91, 149, 88)
_green = (91, 149, 0)
light_python_grey = (60, 63, 65)
dark_python_grey = (43, 43, 43)
pink = (240, 60, 123)

# setup game loop with exit
running = True
while running:

    game_board.fill(light_python_grey)

    # iterate trough events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != 2:
                direction = 1
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != 1:
                direction = 2
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != 4:
                direction = 3
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != 3:
                direction = 4

    snake_position = snake_position[-1:] + snake_position[:-1]




    # draw snake
    for i in range(len(snake_position)):
        if i % 2 == 0:
            pygame.draw.circle(game_board, green, (snake_position[i][0], snake_position[i][1]), cell_size / 2)
        else:
            pygame.draw.circle(game_board, orange, (snake_position[i][0], snake_position[i][1]), cell_size / 2)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     snake_head_rect.x -= 20
    # if keys[pygame.K_RIGHT]:
    #     snake_head_rect.x += 20
    # if keys[pygame.K_UP]:
    #     snake_head_rect.y -= 20
    # if keys[pygame.K_DOWN]:
    #     snake_head_rect.y += 20

    # game_board.blit(player_image, snake_head_rect)  # Draw the player image at its current position
    pygame.display.flip()
    # pygame.display.update()
    clock.tick(10)

pygame.display.flip()

pygame.quit()
