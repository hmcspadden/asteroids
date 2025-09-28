import pygame
import sys
from constants import *
from player import *
from asteroid import * 
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player1 = Player(x, y)
    asteroidfield1 = AsteroidField()
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        player1.timer -= dt
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.kill()
                    shot.kill()
            if asteroid.collision(player1):
                print("Game over!")
                sys.exit()
        for item in drawable:
            item.draw(screen)
        #player1.update(dt)
        #player1.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    
    '''print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")'''


if __name__ == "__main__":
    main()
