import pygame
import sys
import time

from src.settings import Settings
from src.player import Player
from src.maze import create_grid, generate_maze 

class Game:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Pixel Explorer")

        self.clock = pygame.time.Clock()
        self.running = True

        self.last_time = time.time()
        self.dt = 0

        self.player = Player(20, 20)

        self.grid = create_grid(self.settings.screen_width, self.settings.screen_height,
                                self.settings.screen_width // 40,
                                self.settings.screen_height // 40, 40)
        generate_maze(self.grid)

    def run(self):
        while self.running:
            self._dt()
            self._check_events()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        self.player.update(self.dt)
        self.player.render(self.screen)

        for row in self.grid:
            for cell in row:
                cell.draw(self.screen)

        pygame.display.flip()

    def _dt(self):
        self.dt = time.time() - self.last_time
        self.dt *= 60
        self.last_time = time.time()
