import pygame
import circleshape
from constants import PLAYER_RADIUS

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

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

