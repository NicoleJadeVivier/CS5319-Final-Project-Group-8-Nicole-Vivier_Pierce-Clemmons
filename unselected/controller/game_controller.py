import pygame


class GameController:
    def __init__(self, logic, view):
        self.logic = logic
        self.view = view

    def handle_events(self, player, logic):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if logic.state == 'start':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.view.is_over_start(event.pos):
                        self.logic.start_game()

            elif logic.state == 'playing':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.moving_left = True
                    elif event.key == pygame.K_RIGHT:
                        player.moving_right = True
                    elif event.key == pygame.K_SPACE:
                        self.logic.shoot()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.moving_left = False
                    elif event.key == pygame.K_RIGHT:
                        player.moving_right = False
                
            elif logic.state == 'game_over':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.view.is_over_button(event.pos):
                        self.reset_game(logic)

    def reset_game(self, logic):
        # Reset the game logic to its initial state
        logic.start_game()