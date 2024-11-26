import pygame
import circleshape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt    

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if dt != 0:
                self.rotate(-dt)
            else:
                self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        '''
        The screen object
        A color (use "white")
        A list of points (use self.triangle() that we provided for you)
        A line width (use 2)
        '''
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

