from grid import Grid
from bricks import *
import random


class Game:
    def __init__(self):
        self.grid = Grid()
        self.bricks = [IBrick(), JBrick(), LBrick(), OBrick(), SBrick(), ZBrick(), TBrick()]
        self.current_brick = self.get_random_brick()
        self.next_brick = self.get_random_brick()

    def get_random_brick(self):
        if len(self.bricks) == 0:
            self.bricks = [IBrick(), JBrick(), LBrick(), OBrick(), SBrick(), ZBrick(), TBrick()]
        brick = random.choice(self.bricks)
        self.bricks.remove(brick)
        return brick

    def move_left(self):
        self.current_brick.move(0, -1)
        if not self.brick_inside():
            self.current_brick.move(0, 1)

    def move_right(self):
        self.current_brick.move(0, 1)
        if not self.brick_inside():
            self.current_brick.move(0, -1)

    def move_down(self):
        self.current_brick.move(1, 0)
        if not self.brick_inside() or not self.block_fits():
            self.current_brick.move(-1, 0)
            self.lock_brick()

    def lock_brick(self):
        tiles = self.current_brick.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.col] = self.current_brick.id
        self.current_brick = self.next_brick
        self.next_brick = self.get_random_brick()

    def block_fits(self):
        tiles = self.current_brick.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.col):
                return False
            return True

    def rotate(self):
        self.current_brick.rotate()
        if not self.brick_inside():
            self.current_brick.undo_rotation()

    def brick_inside(self):
        tiles = self.current_brick.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside_the_grid(tile.row, tile.col):
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_brick.draw(screen)
