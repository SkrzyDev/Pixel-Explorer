import pygame
import sys
import time

from src.settings import Settings
from src.player import Player

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

        pygame.display.flip()

    def _dt(self):
        self.dt = time.time() - self.last_time
        self.dt *= 60
        self.last_time = time.time()
