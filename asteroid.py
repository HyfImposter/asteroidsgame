import pygame
import circleshape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_split_angle = random.uniform(20, 50)
            split_1_vector = self.velocity.rotate(rand_split_angle)
            split_2_vector = self.velocity.rotate(-rand_split_angle)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            split_1 = Asteroid(self.position[0], self.position[1], split_radius)
            split_2 = Asteroid(self.position[0], self.position[1], split_radius)
            split_1.velocity = split_1_vector * 1.2
            split_2.velocity = split_2_vector * 1.2


        # we need to use random.uniform(a, b) to generate random angle between 20 and 50 deg
    

