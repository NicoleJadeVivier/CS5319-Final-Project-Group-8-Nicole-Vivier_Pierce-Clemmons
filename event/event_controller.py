import pygame
from logic.game_logic import GameLogic
from view.game_view import GameView
from controller.game_controller import GameController
from entities.player import Player
from entities.enemy import Enemy
from entities.bullet import Bullet

def event_controller():
    view = GameView()
    player = Player()
    enemies = []
    player_bullets = []
    enemy_bullets = []
    logic = GameLogic(player,enemies,player_bullets,enemy_bullets)
    view.set_logic(logic)
    

    controller = GameController(logic, view)

    clock = pygame.time.Clock()


    while True:
        controller.handle_events(player, logic)
        logic.update()
        player.update()
        for enemy in enemies.copy():
            bullet = enemy.update()
            if bullet:
                enemy_bullets.append(bullet)
            if enemy.is_out_of_bounds():
                enemy.change_direction()
        for bullet in player_bullets.copy():
            bullet.update()
        for bullet in enemy_bullets.copy():
            bullet.update()
        view.render()
        clock.tick(60)