import pygame

class Player:
    def __init__(self, x, y, speed=3):
        self.x = x
        self.y = y
        self.speed = speed

        self.image = pygame.image.load("assets/images/player.png")
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def move(self, dx, dy, grid, cell_size, dt):
        new_rect = self.rect.move(dx * self.speed * dt, dy * self.speed * dt)
        if not self.collides(new_rect, grid, cell_size):
            self.rect = new_rect
            self.check_key_pickup()
            self.check_door_open()

    def collides(self, rect, grid, cell_size):
        cell_x, cell_y = rect.centerx // cell_size, rect.centery // cell_size
        cell = grid[cell_x][cell_y]

        if rect.left < cell.x * cell_size and cell.walls['W']:
            return True
        if rect.right > (cell_x + 1) * cell_size and cell.walls['E']:
            return True
        if rect.top < cell_y * cell_size and cell.walls['N']:
            return True
        if rect.bottom > (cell_y + 1) * cell_size and cell.walls['S']:
            return True
        
        return False

    def check_key_pickup(self):
        pass
    
    def check_door_open(self):
        pass

    def update(self, grid, cell_size, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.move(-1, 0, grid, cell_size, dt)
        if keys[pygame.K_d]:
            self.move(1, 0, grid, cell_size, dt)
        if keys[pygame.K_w]:
            self.move(0, -1, grid, cell_size, dt)
        if keys[pygame.K_s]:
            self.move(0, 1, grid, cell_size, dt)

    def render(self, screen):
        screen.blit(self.image, self.rect)