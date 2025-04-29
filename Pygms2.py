import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

background_image = pygame.transform.scale(
    pygame.image.load('D:\main\pygms\IMG-worlds-of-adventure.webp').convert_alpha(),
    (SCREEN_WIDTH, SCREEN_HEIGHT))

text = pygame.font.Font(None, 36).render('ROller coaster', True ,pygame.Color('black'))

text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()