import pygame
from constants import *
from  circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from sys import exit

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 #Delta Time

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        # player.update(dt)
        # player.draw(screen)
        for i in updatable:
            i.update(dt)
        for i in drawable:
            i.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over")
                exit()
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()

        #limit framerate to 60 fps
        dt = clock.tick(60)/1000 


if __name__ == "__main__":
    main()
