from .entities.player import Player
from .entities.enemy import Enemy


class GameModel:
    def __init__(self):
        self.state = 'start'
        self.player = Player()
        self.enemies = []
        self.player_bullets = []
        self.enemy_bullets = []
        self.score = 0
        self.game_over = False

    def start_game(self):
        self.state = 'playing'
        self.player = Player()
        self.enemies = [Enemy(x, 100 + 40 * y, 0.5 if x % 2 == 0 else -0.5) for x in range(50, 750, 100) for y in range(3)]
        self.player_bullets = []
        self.enemy_bullets = []
        self.score = 0
        self.game_over = False

    def update(self):
        if self.state != 'playing' or self.game_over:
            return

        self.player.update()
        for bullet in self.player_bullets.copy():
            bullet.update()
            if bullet.is_out_of_bounds():
                self.player_bullets.remove(bullet)
            else:
                for enemy in self.enemies:
                    if bullet.collides_with(enemy):
                        self.enemies.remove(enemy)
                        self.player_bullets.remove(bullet)
                        self.score += 10
                        break

        if not self.enemies:
            self.game_over = True
            self.state = 'game_over'
            return

        for enemy in self.enemies.copy():
            bullet = enemy.update()
            if bullet:
                self.enemy_bullets.append(bullet)
            if enemy.is_out_of_bounds():
                enemy.change_direction()

        for bullet in self.enemy_bullets.copy():
            bullet.update()
            if bullet.collides_with(self.player):
                self.game_over = True
                self.state = "game_over"
                return
            if bullet.is_out_of_bounds():
                self.enemy_bullets.remove(bullet)

    def shoot(self):
        if not self.game_over:
            self.player_bullets.append(self.player.shoot())