import random
from random import choice,randint

bricks = ['o', 'i', 's', 'z', 'l', 'j', 't']
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1],
     [0, 1, 0]],     # T
    [[1, 1],
     [1, 1]],         # O
    [[0, 1, 1],
     [1, 1, 0]],      # S
    [[1, 1, 0],
     [0, 1, 1]],      # Z
    [[1, 1, 1],
     [1, 0, 0]],      # L
    [[1, 1, 1],
     [0, 0, 1]]       # J
]





def get_random_brick_in_random_position():
    selected_brick = random.choice(bricks)

    return selected_position


print(get_random_brick_in_random_position())
