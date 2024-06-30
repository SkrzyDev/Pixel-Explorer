import pygame
import sys

from src.settings import Settings

class Game:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Pixel Explorer")

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
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
        pygame.display.flip()
