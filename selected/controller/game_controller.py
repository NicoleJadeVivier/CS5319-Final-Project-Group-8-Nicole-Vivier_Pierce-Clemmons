import pygame


class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if self.model.state == 'start':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.view.is_over_start(event.pos):
                        self.model.start_game()

            elif self.model.state == 'playing':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.model.player.moving_left = True
                    elif event.key == pygame.K_RIGHT:
                        self.model.player.moving_right = True
                    elif event.key == pygame.K_SPACE:
                        self.model.shoot()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.model.player.moving_left = False
                    elif event.key == pygame.K_RIGHT:
                        self.model.player.moving_right = False
            elif self.model.state == 'game_over':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.view.is_over_button(event.pos):
                        self.reset_game()

    def reset_game(self):
        # Reset the game model to its initial state
        self.model.__init__()
        self.model.start_game()