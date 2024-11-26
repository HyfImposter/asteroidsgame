import pygame
from constants import *
from player import Player

'''
Check for player inputs
Update the game world
Draw the game to the screen
'''


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x, y)
    # we need to set our game FPS as 60
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(0,0,0))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 # it will pause the game loop until 1/60 second has passed
        
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
