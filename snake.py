import pygame


class Snake:

    def __init__(self, surface) -> None:
        self.surface = surface
        self.x = 30
        self.y = 4
        self.direction = (0, 1)
        self.trace = [(self.x - self.direction[0]*i, self.y - self.direction[1]*i) for i in range(6)]
        self.growCount = 0

    def draw(self):
        for z in self.trace:
            x, y = z
            pygame.draw.rect(self.surface, (255,255,255), [x*10, y*10, 10, 10], 2)

    def move(self):
        x, y = self.trace[0]
        x, y = (x + self.direction[0]) % 80, (y + self.direction[1]) % 60
        self.trace.insert(0, (x, y))
        if not self.growCount:
            self.trace.pop()
        else:
            self.growCount -= 1

    @property
    def head(self):
        return self.trace[0]
    
    def grow(self, n=1):
        self.growCount += n

    def changeDirection(self, vector):
        if self.direction[0]*vector[0]+self.direction[1]*vector[1]==0:
            self.direction = vector

    def checkCollision(self) -> bool:
        return self.head in self.trace[1:]