import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Shapes
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

SHAPE_COLORS = [CYAN, MAGENTA, YELLOW, GREEN, RED, ORANGE, BLUE]

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Create grid
def create_grid():
    return [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]

# Draw the grid
def draw_grid(grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(screen, BLACK, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
            if grid[y][x]:
                pygame.draw.rect(screen, SHAPE_COLORS[grid[y][x] - 1],
                                 (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Check if a shape can fit
def check_collision(shape, offset, grid):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                grid_x = x + offset[0]
                grid_y = y + offset[1]
                if (grid_x < 0 or grid_x >= GRID_WIDTH or
                        grid_y >= GRID_HEIGHT or grid[grid_y][grid_x]):
                    return True
    return False

# Merge shape into the grid
def merge_shape(shape, offset, grid, color_index):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                grid[y + offset[1]][x + offset[0]] = color_index

# Remove full lines
def remove_lines(grid):
    new_grid = [row for row in grid if any(cell == 0 for cell in row)]
    num_lines = GRID_HEIGHT - len(new_grid)
    return [[0] * GRID_WIDTH] * num_lines + new_grid

# Main game loop
def main():
    clock = pygame.time.Clock()
    grid = create_grid()
    current_shape = random.choice(SHAPES)
    shape_color_index = SHAPE_COLORS.index(random.choice(SHAPE_COLORS)) + 1
    shape_pos = [GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0]
    drop_time = 0
    run_game = True

    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            shape_pos[0] -= 1
            if check_collision(current_shape, shape_pos, grid):
                shape_pos[0] += 1

        if keys[pygame.K_RIGHT]:
            shape_pos[0] += 1
            if check_collision(current_shape, shape_pos, grid):
                shape_pos[0] -= 1

        if keys[pygame.K_DOWN]:
            shape_pos[1] += 1
            if check_collision(current_shape, shape_pos, grid):
                shape_pos[1] -= 1

        if keys[pygame.K_UP]:
            rotated_shape = list(zip(*current_shape[::-1]))
            if not check_collision(rotated_shape, shape_pos, grid):
                current_shape = rotated_shape

        drop_time += clock.get_rawtime()
        clock.tick()
        if drop_time > 500:
            drop_time = 0
            shape_pos[1] += 1
            if check_collision(current_shape, shape_pos, grid):
                shape_pos[1] -= 1
                merge_shape(current_shape, shape_pos, grid, shape_color_index)
                grid = remove_lines(grid)
                current_shape = random.choice(SHAPES)
                shape_color_index = SHAPE_COLORS.index(random.choice(SHAPE_COLORS)) + 1
                shape_pos = [GRID_WIDTH // 2 - len(current_shape[0]) // 2, 0]
                if check_collision(current_shape, shape_pos, grid):
                    run_game = False

        screen.fill(WHITE)
        draw_grid(grid)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()