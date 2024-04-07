import pygame


class GameView:
    def __init__(self):
        pygame.display.set_caption("Galaga")
        self.screen = pygame.display.set_mode((800, 600))
        self.game_over_font = pygame.font.Font(None, 48)
        self.play_again_font = pygame.font.Font(None, 36)
        self.score_font = pygame.font.Font(None, 36)
        self.play_again_rect = pygame.Rect(310, 340, 200, 50)
        self.start_button_rect = pygame.Rect(300, 250, 215, 50)
        self.logic = None

        self.logo_image = pygame.image.load('././selected/graphics/galagaLogo.png').convert_alpha()
        self.logo_image = pygame.transform.scale(self.logo_image, (300, 150))  # Adjust size as needed
        self.logo_pos = self.logo_image.get_rect(center=(400, 150))

    def set_logic(self, logic):
        self.logic = logic

    def render(self):
        self.screen.fill((0, 0, 0))

        if self.logic.state == 'start':
            self.screen.blit(self.logo_image, self.logo_pos)

            start_text = self.game_over_font.render('Start Game', True, (255, 255, 255))
            pygame.draw.rect(self.screen, (64, 224, 208), self.start_button_rect)  # Button background
            self.screen.blit(start_text, (self.start_button_rect.x + 20, self.start_button_rect.y + 10))
            mouse_pos = pygame.mouse.get_pos()

            if self.start_button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, (0, 0, 0), self.start_button_rect)  # Highlight background
                self.screen.blit(start_text, (self.start_button_rect.x + 20, self.start_button_rect.y + 10))
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.draw.rect(self.screen, (0, 0, 0), self.play_again_rect)
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        elif self.logic.state == 'playing':
            self.screen.blit(self.logic.player.image, self.logic.player.pos)
            for enemy in self.logic.enemies:
              self.screen.blit(enemy.image, enemy.pos)
            for bullet in self.logic.player_bullets + self.logic.enemy_bullets:
                self.screen.blit(bullet.image, bullet.pos)

            score_text = self.score_font.render(f'Score: {self.logic.score}', True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))

        elif self.logic.state == 'game_over':
            game_over_text = self.game_over_font.render('Game Over', True, (255, 0, 0))
            self.screen.blit(game_over_text, (315, 200))

            score_text = self.score_font.render(f'Score: {self.logic.score}', True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))

            mouse_pos = pygame.mouse.get_pos()
            if self.play_again_rect.collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, (100, 100, 100), self.play_again_rect)  # Highlight background
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.draw.rect(self.screen, (0, 0, 0), self.play_again_rect)
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            play_again_text = self.play_again_font.render('Play Again', True, (64, 224, 208))
            pygame.draw.rect(self.screen, (0, 0, 0), self.play_again_rect)
            self.screen.blit(play_again_text, (self.play_again_rect.x + 30, self.play_again_rect.y + 5))

        pygame.display.flip()

    def is_over_button(self, pos):
        return self.play_again_rect.collidepoint(pos)

    def is_over_start(self, pos):
        return self.start_button_rect.collidepoint(pos)