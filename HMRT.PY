import pygame

pygame.init()
screen = pygame.display.set_mode((400,500))
Done = False
while not Done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True

    pygame.draw.rect(screen,(200,230,255) , pygame.Rect(30,30,120,120))

    pygame.display.flip()