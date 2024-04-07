import pygame
from logic.game_logic import GameLogic
from view.game_view import GameView
from controller.game_controller import GameController
from entities.player import Player


class EventController():
    def __init__(self):
        self.view = GameView()
        self.player = Player()
        self.enemies = []
        self.player_bullets = []
        self.enemy_bullets = []
        self.logic = GameLogic(self.player,self.enemies,
                               self.player_bullets,self.enemy_bullets)
        self.view.set_logic(self.logic)
        

        self.controller = GameController(self.logic, self.view)

        self.clock = pygame.time.Clock()


    def notify(self):
        while True:
            self.controller.handle_events(self.player, self.logic)
            self.logic.update()
            self.player.update()
            for enemy in self.enemies.copy():
                bullet = enemy.update()
                if bullet:
                    self.enemy_bullets.append(bullet)
                if enemy.is_out_of_bounds():
                    enemy.change_direction()
            for bullet in self.player_bullets.copy():
                bullet.update()
            for bullet in self.enemy_bullets.copy():
                bullet.update()
            self.view.render()
            self.clock.tick(60)