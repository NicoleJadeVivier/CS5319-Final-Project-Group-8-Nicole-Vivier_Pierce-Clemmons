import random
import pygame
from .bullet import Bullet


class Enemy:
    def __init__(self, x, y, speed):
        self.image = pygame.image.load('././graphics/enemyShip.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 50))
        self.pos = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        self.pos.x += self.speed
        bullet = None
        if self.is_out_of_bounds():
            self.pos.y += 20  # Move down a bit when wrapping around
            self.pos.x = 0 if self.pos.x > 800 else 800  # Wrap position to the opposite side

        if random.random() < 0.001:  # Adjust for shooting frequency
            bullet = Bullet(self.pos.centerx, self.pos.bottom, 1)  # Enemy bullets move down

        return bullet

    def is_out_of_bounds(self):
        return self.pos.right < 0 or self.pos.left > 800

    def change_direction(self):
        self.speed = -self.speed
        self.pos.y += 20