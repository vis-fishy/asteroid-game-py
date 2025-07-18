from circle_shapes import *
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import SHOT_RADIUS
from constants import PLAYER_SHOT_SPEED
from constants import PLAYER_SHOT_COOLDOWN

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    
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
        self.timer -= dt
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shot(self):
        new_shot = Shot(self.position.x, self.position.y) # type: ignore
        new_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        self.timer = PLAYER_SHOT_COOLDOWN

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt