import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

class sprite(pygame.sprite.Sprite):
    def __init__(self, color, pos):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)

    def change_color(self):
        self.image.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))

s1 = sprite((255, 0, 0), (100, 150))
s2 = sprite((0, 255, 0), (300, 150))
group = pygame.sprite.Group(s1, s2)

changecolor = pygame.USEREVENT + 1
pygame.time.set_timer(changecolor, 1000)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == changecolor:
            for s in group:
                s.change_color()

    screen.fill((0, 0, 0))
    group.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()