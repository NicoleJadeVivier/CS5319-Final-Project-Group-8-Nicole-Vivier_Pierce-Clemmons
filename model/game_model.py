from .entities.player import Player
from .entities.enemy import Enemy


class GameModel:
    def __init__(self, player, enemies,player_bullets,enemy_bullets):
        self.state = 'start'
        self.player = player
        self.enemies = enemies
        self.player_bullets = player_bullets
        self.enemy_bullets = enemy_bullets
        self.score = 0
        self.game_over = False

    def start_game(self):
        self.state = 'playing'
        spawn_enemies = [Enemy(x, 100 + 40 * y, 0.5 if x % 2 == 0 else -0.5) for x in range(50, 750, 100) for y in range(3)]
        del self.enemies[:]
        for enemy in spawn_enemies:
            self.enemies.append(enemy)
        del self.enemy_bullets[:]
        del self.player_bullets[:]
        self.score = 0
        self.game_over = False

    def update(self):
        if self.state != 'playing' or self.game_over:
            return

        for bullet in self.player_bullets.copy():
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
            spawn_enemies = [Enemy(x, 100 + 40 * y, speed=self.score/400) for x in range(50, 750, 100) for y in range(3)]
            for enemy in spawn_enemies:
                self.enemies.append(enemy)
            return            

        for bullet in self.enemy_bullets.copy():
            if bullet.collides_with(self.player):
                self.game_over = True
                self.state = "game_over"
                return
            if bullet.is_out_of_bounds():
                self.enemy_bullets.remove(bullet)

    def shoot(self):
        if not self.game_over:
            self.player_bullets.append(self.player.shoot())