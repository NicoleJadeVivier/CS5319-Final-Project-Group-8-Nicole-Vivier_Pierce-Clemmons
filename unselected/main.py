import pygame

from event.event_controller import EventController


def main():
    pygame.init()

    event = EventController()
    event.notify()

if __name__ == "__main__":
    main()
