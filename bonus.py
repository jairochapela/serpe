import random

import pygame

COLORS = [(255,0,0), (255,255,0), (0,255,0), (0,255,255), (0, 0, 255), (255,0,255)]

class Bonus:
    def __init__(self, surface, x, y) -> None:
        self.surface = surface
        self.x = x
        self.y = y
        self.color = random.choice(COLORS)
        self.ttl = sum([random.randint(1, 100) for _ in range(3)])

    def draw(self):
        pygame.draw.rect(self.surface, self.color, [self.x*10, self.y*10, 10, 10], 2)

    def update(self):
        self.ttl -= 1

    @property
    def position(self):
        return (self.x, self.y)
    
    @property
    def podre(self):
        return self.ttl < 0
