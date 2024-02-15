import pygame
import sys

pygame.init()

width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Color Change on Hover")

white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)

rect_size = 100


class Square():
    def __init__(self, width, height, rect_size):
        self.rect = pygame.Rect(width, height, rect_size, rect_size)
        self.color = black
    def update_color(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.color = gray
        else:
            self.color = black
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


squares = [
    Square(0, 0, rect_size-1),
    Square(0, rect_size,rect_size-1),
    Square(rect_size, 0, rect_size-1),
    Square(rect_size,rect_size, rect_size-1),
    Square(2 * rect_size, 2 * rect_size, rect_size-1),
    Square(2 * rect_size, 0, rect_size-1),
    Square(0, 2*rect_size, rect_size-1),
    Square(rect_size, 2*rect_size, rect_size-1),
    Square(2*rect_size, rect_size, rect_size-1)
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mouse_position = pygame.mouse.get_pos()

    for square in squares:
        square.update_color(mouse_position)

    screen.fill((255, 255, 255))

    for square in squares:
        square.draw(screen)

    pygame.display.flip()

    pygame.time.Clock().tick(60)