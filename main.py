import pygame
from model.game_model import GameModel
from view.game_view import GameView
from controller.game_controller import GameController


def main():
    pygame.init()

    view = GameView()
    model = GameModel()
    view.set_model(model)

    controller = GameController(model, view)

    clock = pygame.time.Clock()

    while True:
        controller.handle_events()
        model.update()
        view.render()
        clock.tick(60)

if __name__ == "__main__":
    main()
