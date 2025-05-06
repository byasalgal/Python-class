import pygame
import random

pygame.init()

sprite_color_change = pygame.USEREVENT + 1
background_color_change = pygame.USEREVENT + 2


LIGHT_BLUE = pygame.Color('lightblue')
LIGHT_GREEN = pygame.Color('lightgreen')
LIGHT_ORANGE = pygame.Color((240,150,150))

BLUE = pygame.Color('blue')
GREEN = pygame.Color('green')
ORANGE = pygame.Color('orange')

class SPRITE(pygame.sprite.Sprite):

    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]) , random.choice([-1,1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 1920:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
    
        if self.rect.top <= 0 or self.rect.bottom >= 1080:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_color_change))
            pygame.event.post(pygame.event.Event(background_color_change))

    def change_color(self):
        self.image.fill(random.choice([BLUE,GREEN,ORANGE]))

def change_background_color():
    global bg_color
    bg_color = random.choice([LIGHT_BLUE,LIGHT_GREEN,LIGHT_ORANGE])

all_sprite_list = pygame.sprite.Group()
sp1 = SPRITE(LIGHT_BLUE,20,30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
all_sprite_list.add(sp1)
screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Boundary Sprite")
bg_color = BLUE
screen.fill(bg_color)
exit = False
clock=pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == sprite_color_change:

            sp1.change_color()
        elif event.type == background_color_change:
            change_background_color()

    all_sprite_list.update()
    screen.fill(bg_color)
    all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(240)

pygame.quit