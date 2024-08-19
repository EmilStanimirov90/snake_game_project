import random
from random import choice

bricks = ['o', 'i', 's', 'z', 'l', 'j', 't']
bricks_positions = {'o': [[1, 1], [1, 2], [2, 1], [2, 2]]}


#          'i':([1,1],[1,2],[1,3],[1,4]),
#          's':([2,1],[2,2],[1,2],[1,3]),
#         'z':([1,1],[1,2],[1,2],[1,3]),
#         'l',
#         'j',
#         't'}


def get_random_brick_in_random_position():
    selected_brick = random.choice(bricks)
    selected_position = random.choice(bricks_positions[selected_brick])
    return selected_position


print(get_random_brick_in_random_position())
