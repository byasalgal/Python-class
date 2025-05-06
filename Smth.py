import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

WHITE = (255, 255, 255)
RECT_COLOR = (0, 128, 255)
TEXT_COLOR = (0, 0, 0)

font = pygame.font.SysFont(None, 48)
text = font.render("hello, pygame!", True, TEXT_COLOR)
text_rect = text.get_rect(center=(320, 240))

rect_width, rect_height = 200, 100
rect = pygame.Rect((640 - rect_width) // 2, (480 - rect_height) // 2, rect_width, rect_height)

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, RECT_COLOR, rect)
    screen.blit(text, text_rect)
    pygame.display.update()

pygame.quit()