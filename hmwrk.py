import pygame
pygame.init()
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
grey = (58, 58, 58)
image = pygame.image.load("D:\main\pygms\IMG-worlds-of-adventure.webp")  # Must be in same folder
image = pygame.transform.scale(image, (300, 300))
image_rect = image.get_rect(center=(window_size[0] // 2, window_size[1] // 2))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(grey)
    screen.blit(image, image_rect)
    pygame.display.update()

pygame.quit()
