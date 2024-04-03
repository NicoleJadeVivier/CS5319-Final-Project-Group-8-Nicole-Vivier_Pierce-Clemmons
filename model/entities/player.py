import pygame
from .bullet import Bullet


class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 30))
        self.image.fill((0, 255, 0))
        self.pos = self.image.get_rect(center=(400, 550))
        self.speed = 5
        self.moving_left = False
        self.moving_right = False

    def move_left(self):
        self.pos.centerx -= 5

    def move_right(self):
        self.pos.centerx += 5

    def update(self):
        if self.moving_left:
            self.pos.x = max(0, self.pos.x - self.speed)
        if self.moving_right:
            self.pos.x = min(800 - self.pos.width, self.pos.x + self.speed)

    def shoot(self):
        return Bullet(self.pos.centerx, self.pos.top, -1)