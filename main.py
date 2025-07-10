import pygame

from constants import *
from circle_shapes import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))

        player.draw(screen)
        player.update(dt)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
    pygame.sprite.Sprite()
