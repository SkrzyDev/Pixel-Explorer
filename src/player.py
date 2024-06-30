import pygame

class Player:
    def __init__(self, x, y, speed=3):
        self.x = x
        self.y = y
        self.speed = speed

        self.image = pygame.image.load("assets/images/player.png")
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]: self.y -= self.speed * dt
        if keys[pygame.K_s]: self.y += self.speed * dt
        if keys[pygame.K_a]: self.x -= self.speed * dt
        if keys[pygame.K_d]: self.x += self.speed * dt

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))