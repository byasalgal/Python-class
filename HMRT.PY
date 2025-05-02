import pygame

pygame.init()
screen = pygame.display.set_mode((400,500))
screen.fill((0,0,0))

pygame.draw.circle(screen , (200,220,255) , (300,300) ,50,)
pygame.draw.circle(screen , (200,220,255) , (100,100) ,50,3)
Done = False
while not Done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True

    pygame.display.flip()