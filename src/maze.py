import pygame
import random

# Settings
WIDTH, HEIGHT = 800, 600

# Maze settings (default)
COLS, ROWS = 10, 10
CELL_SIZE = WIDTH // COLS

# Maze variables
DIRECTIONS = {
    'N': (0, -1),
    'S': (0, 1),
    'E': (1, 0),
    'W': (-1, 0)
}
OPPOSITE = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

# Maze generation
"""
To create the maze firstly create a grid of cells, where each cell can have
walls on its north, south, east, and west sides.
Start with all walls intact

To generate a maze:
- Pick a starting cell and mark it as visited.
- While there are unvisited cells:
    - Choose a random unvisited neighboring cell.
    - Remove the wall between the current cell and the chosen cell.
    - Move to the chosen cell and mark it as visited.
    - If there are no unvisited neigboring cells, backtrack to the previous
    cell with unvisited neighbors and continue.
"""
class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.visited = False
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}

    def draw(self, screen):
        x, y = self.x * CELL_SIZE, self.y * CELL_SIZE
        if self.walls['N']:
            pygame.draw.line(screen, (200, 200, 200), (x, y), (x + CELL_SIZE, y), 2)
        if self.walls['S']:
            pygame.draw.line(screen, (200, 200, 200), (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 2)
        if self.walls['E']:
            pygame.draw.line(screen, (200, 200, 200), (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 2)
        if self.walls['W']:
            pygame.draw.line(screen, (200, 200, 200), (x, y), (x, y + CELL_SIZE), 2)

def create_grid(width, height, rows, cols, cell_size):
    global COLS, ROWS, CELL_SIZE, WIDTH, HEIGHT
    COLS = cols
    ROWS = rows
    CELL_SIZE = cell_size
    WIDTH = width
    HEIGHT = height
    return [[Cell(x, y) for y in range(ROWS)] for x in range(COLS)]

def get_neighbors(cell, grid):
    neighbors = []
    for direction, (dx, dy) in DIRECTIONS.items():
        nx, ny = cell.x + dx, cell.y + dy
        if 0 <= nx < COLS and 0 <= ny < ROWS and not grid[nx][ny].visited:
            neighbors.append((direction, grid[nx][ny]))
    return neighbors

def remove_wall(current, next, direction):
    current.walls[direction] = False
    next.walls[OPPOSITE[direction]] = False

def generate_maze(grid):
    stack = []
    current = grid[0][0]
    current.visited = True

    while True:
        neighbors = get_neighbors(current, grid)
        if neighbors:
            direction, next_cell = random.choice(neighbors)
            remove_wall(current, next_cell, direction)
            stack.append(current)
            current = next_cell
            current.visited = True
        elif stack:
            current = stack.pop()
        else:
            break