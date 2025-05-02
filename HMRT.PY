import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
x, y = 250, 250
radius = 50

Done = False
while not Done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]: y -= 5
    if pressed[pygame.K_s]: y += 5
    if pressed[pygame.K_a]: x -= 5
    if pressed[pygame.K_d]: x += 5

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (x, y), radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()