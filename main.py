import pygame

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while(True):
        screen.fill((0,0,0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
