import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

'''
Check for player inputs
Update the game world
Draw the game to the screen
'''


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
     
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y)
    asteroidsfild = AsteroidField()

    # we need to set our game FPS as 60
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updatable:
            thing.update(dt)

        for obj in asteroids:
            if obj.check_collisions(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.check_collisions(obj):
                    shot.kill()
                    obj.split()
     
        screen.fill(color=(0,0,0))
       
        for thing in drawable:
            thing.draw(screen)
        #player.update(dt)
        #player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # it will pause the game loop until 1/60 second has passed
        
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
