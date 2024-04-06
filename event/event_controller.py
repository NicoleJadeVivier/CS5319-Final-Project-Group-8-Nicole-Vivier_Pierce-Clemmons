import pygame
from model.game_model import GameModel
from view.game_view import GameView
from controller.game_controller import GameController
from model.entities.player import Player
from model.entities.enemy import Enemy
from model.entities.bullet import Bullet

def event_controller():
    view = GameView()
    player = Player()
    enemies = []
    player_bullets = []
    enemy_bullets = []
    model = GameModel(player,enemies,player_bullets,enemy_bullets)
    view.set_model(model)
    

    controller = GameController(model, view)

    clock = pygame.time.Clock()


    while True:
        controller.handle_events(player, model)
        model.update()
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