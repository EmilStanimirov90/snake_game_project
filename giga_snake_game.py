from collections import deque

import pygame
from random import randint


def generate_food_random_position(_x, _y):
    x = randint(0, _x)  # Replace 800 with your desired maximum x-coordinate
    y = randint(0, _y)  # Replace 800 with your desired maximum y-coordinate

    return (x // cell_size) * cell_size, (y // cell_size) * cell_size


pygame.init()

# create screen and name
game_board_x = 800
game_board_y = 800
game_board = pygame.display.set_mode((game_board_x, game_board_y))
pygame.display.set_caption("Giga-Mecha-Snake")

# game variables
cell_size = 20
direction = ""  # 1 is up 2 is down 3 is right 4 is left
moving = False
eaten = True
food_x = 0
food_y = 0
total_score = 0

# create snake
snake_position = deque([[int(game_board_x / 2), int(game_board_y / 2)],
                        [int(game_board_x / 2), int(game_board_y / 2) + cell_size],
                        [int(game_board_x / 2), int(game_board_y / 2) + cell_size * 2],
                        [int(game_board_x / 2), int(game_board_y / 2) + cell_size * 3],
                        [int(game_board_x / 2), int(game_board_y / 2) + cell_size * 4]
                        ])
snake_head = snake_position[0]

# possible moves
moves = {"up": (0, -cell_size), "down": (0, cell_size), "right": (cell_size, 0), "left": (-cell_size, 0)}

# game speed
clock = pygame.time.Clock()
snake_speed = 2

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

# setup game LOOP with exit
running = True
while running:

    game_board.fill(light_python_grey)

    # iterate trough events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != "down":
                direction = "up"
                moving = True
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != "up":
                direction = "down"
                moving = True
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != "left":
                direction = "right"
                moving = True
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != "right":
                direction = "left"
                moving = True
    # move
    if moving:
        snake_position.appendleft([snake_position[0][0] + moves[direction][0], snake_position[0][1] + moves[direction][1]])
        snake_position.pop()

    # generate food and place food
    if eaten:
        food_x, food_y = generate_food_random_position(game_board_x, game_board_y)
        eaten = False

    # place food on game_board
    food = pygame.draw.rect(game_board, pink, (food_x, food_y, cell_size, cell_size))

    # draw snake + moving
    for i in range(len(snake_position)):
        if i % 2 == 0:
            pygame.draw.rect(game_board, green, (snake_position[i][0], snake_position[i][1], cell_size, cell_size))
        else:
            pygame.draw.rect(game_board, orange, (snake_position[i][0], snake_position[i][1], cell_size, cell_size))

    # eating food and growing
    if snake_position[0] == [food_x, food_y]:
        eaten = True
        snake_position.append([food_x, food_y])
        total_score += 1

    #display_score
    score_text = font.render(f"Score: {total_score}", True, )
    game_board.blit(score_text, (10, 10))


    # game_board.blit(player_image, snake_head_rect)  # Draw the player image at its current position
    # pygame.display.flip()
    pygame.display.update()

    clock.tick(snake_speed)
# pygame.display.flip()

pygame.quit()
