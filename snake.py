import pygame


class Snake:

    def __init__(self, surface) -> None:
        self.surface = surface
        self.x = 10
        self.y = 10
        self.trace = [(self.x, self.y)]
        self.direction = (0, 1)

    def draw(self):
        for z in self.trace:
            x, y = z
            pygame.draw.rect(self.surface, (255,255,255), [x, y, 10, 10], 2)

    def move(self):
        x, y = self.trace[0]
        x, y = x + self.direction[0], y + self.direction[1]
        self.trace.insert(0, (x, y))
        self.trace.pop()
