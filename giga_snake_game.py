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
direction = None  # 1 is up 2 is down 3 is right 4 is left
moving = False
eaten = True
food_x = 0
food_y = 0
total_score = 0
game_started = False
game_ended = False


# create snake
snake_position = deque([[int(game_board_x / 2), int(game_board_y / 2)],
                        [int(game_board_x / 2), int(game_board_y / 2) + cell_size],
                        [int(game_board_x / 2), int(game_board_y / 2) + cell_size * 2],
                        [int(game_board_x / 2), int(game_board_y / 2) + cell_size * 3],
                        [int(game_board_x / 2), int(game_board_y / 2) + cell_size * 4]
                        ])

# possible moves
moves = {"up": (0, -cell_size), "down": (0, cell_size), "right": (cell_size, 0), "left": (-cell_size, 0)}

# game speed
clock = pygame.time.Clock()
snake_speed = 8  # 8 is a good normal speed

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
blue = (126, 170, 199)

# font setup
font = pygame.font.Font(None, 36)

# setup game LOOP with exit
running = True
while running:

    game_board.fill(light_python_grey)


    # iterate trough events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # snake keyboard movement key and menu key
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != "down":
                direction = "up"
                game_started = True
                moving = True
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != "up":
                direction = "down"
                game_started = True
                moving = True
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != "left":
                direction = "right"
                game_started = True
                moving = True
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != "right":
                direction = "left"
                game_started = True
                moving = True

    # move
    if moving:
        snake_position.appendleft(
            [snake_position[0][0] + moves[direction][0], snake_position[0][1] + moves[direction][1]])
        snake_position.pop()

    # generate food position and place food
    if eaten:
        correct_position_found = False
        while not correct_position_found:
            food_x, food_y = generate_food_random_position(game_board_x, game_board_y)
            for x, y in snake_position:
                if food_x == x or food_y == y:
                    break
            else:
                correct_position_found = True
        eaten = False

    # place food on game_board
    food = pygame.draw.rect(game_board, pink, (food_x, food_y, cell_size, cell_size))

    # draw snake + moving
    for i in range(len(snake_position)):
        if i % 2 == 0:
            pygame.draw.rect(game_board, green, (snake_position[i][0], snake_position[i][1], cell_size, cell_size))
        else:
            pygame.draw.rect(game_board, orange, (snake_position[i][0], snake_position[i][1], cell_size, cell_size))

    # eating food and growing and increasing the speed
    if snake_position[0] == [food_x, food_y]:
        eaten = True
        snake_position.append(snake_position[-1])
        total_score += 1
        snake_speed += 0.1

    # display_score
    score_rect = font.render(f"Total score: {total_score * 10}", True, blue)
    game_board.blit(score_rect, (0, 0))

    # display controls before game start
    if not game_started:
        starting_message = font.render(f"Press W,A,S,D or the arrow keys to start game", True, blue)
        game_board.blit(starting_message, (150, 600))

    # Game over if snake collides with border walls
    if snake_position[0][0] not in range(0, game_board_x) or snake_position[0][1] not in range(0, game_board_y):
        game_ended = True

    # Game over if snake collides with self
    for i in range(1, len(snake_position)):
        if snake_position[0] == snake_position[i]:
            game_ended = True

    if game_ended:
        game_board.fill(light_python_grey)
        end_message = font.render(f"Your score is: {total_score}", True, blue)
        game_board.blit(end_message, (300, 400))

    # game_board.blit(player_image, snake_head_rect)  # Draw the player image at its current position
    # pygame.display.flip()
    pygame.display.update()

    clock.tick(snake_speed)
# pygame.display.flip()

pygame.quit()
