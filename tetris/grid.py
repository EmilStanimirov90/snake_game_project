import pygame
from colors import Colors



class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def is_inside_the_grid(self, row, col):
        if 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            return True
        return False

    def is_empty(self, row, col):
        if self.grid[row][col] == 0:
            return True
        return False

    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                cell_rect = pygame.Rect(col * self.cell_size + 1, row * self.cell_size + 1,
                                        self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
