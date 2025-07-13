import pygame
import sys

from constants import *
from circle_shapes import *
from player import *
from asteroids import *
from asteroid_field import *

def copy_without(item, group):
    copy = pygame.sprite.Group.copy(group)
    copy.remove(item)
    return copy

def main():
    pygame.init()

    score = 0

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))

    shot = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable) # type: ignore
    Asteroid.containers = (asteroid, updateable, drawable) # type: ignore
    AsteroidField.containers = (updateable) # type: ignore
    Shot.containers = (shot, updateable, drawable) # type: ignore

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()
    
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

        for obj in drawable:
            obj.draw(screen)
        updateable.update(dt)

        for obj in asteroid:
            if (obj.collisions(player)):
                print("Game Over")
                print(f"Score: {score}")
                sys.exit()
        for obj1 in asteroid:
            for obj2 in shot:
                if (obj1.collisions(obj2)):
                    obj1.split()
                    obj2.kill()
                    score += 1
        
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
    pygame.sprite.Sprite()


