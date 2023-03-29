import pygame


class Snake:

    def __init__(self, surface) -> None:
        self.surface = surface
        self.trace = [(10, 10)]
        self.direction = (0, 1)

    def draw(self):
        pygame.draw.rect(self.surface, (255,255,255), [self.x, self.y, self.x+10, self.y+10], 2)

    def move(self):
        x, y = self.trace[0]
        x, y += self.direction
        self.trace.insert(0, (x, y))
        self.trace.pop()
