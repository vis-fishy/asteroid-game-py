from circle_shapes import *
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED

class Player(CircleShape):
    rotation = 0.0

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + self.radius * forward
        b = self.position - self.radius * forward - right
        c = self.position - self.radius * forward + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)