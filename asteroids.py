import pygame
import random

from constants import *
from circle_shapes import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self, ast=False):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            generate = random.uniform(20,50)
            v1 = self.velocity.rotate(generate)
            v2 = self.velocity.rotate(-generate)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast1, ast2 = Asteroid(self.position.x, self.position.y, new_radius), Asteroid(self.position.x, self.position.y, new_radius) # type: ignore
            ast1.velocity = v1 * ASTEROID_SPEED_MULTIPLY
            ast2.velocity = v2 * ASTEROID_SPEED_MULTIPLY
    