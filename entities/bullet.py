import pygame


class Bullet:
    def __init__(self, x, y, direction):
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 255))
        self.pos = self.image.get_rect(center=(x, y))
        self.direction = direction  # positive for down, negative for up

    def update(self):
        self.pos.y += (10 * self.direction)

    def is_out_of_bounds(self):
        return self.pos.top <= 0 or self.pos.bottom >= 600

    def collides_with(self, sprite):
        return self.pos.colliderect(sprite.pos)