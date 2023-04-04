import random
import pygame

from bonus import Bonus

class Field:
    def __init__(self, surface) -> None:
        self.surface = surface
        #self.walls = []
        self.walls = [(k,0) for k in range(80)] + [(k,59) for k in range(80)] + [(0,k) for k in range(60)] + [(79,k) for k in range(60)]
        self.bonus = [Bonus(surface, random.randint(1,78), random.randint(1,58)) for _ in range(3)]

    def draw(self):
        self.surface.fill((0,0,0))
        for w in self.walls:
            x, y = w
            pygame.draw.rect(self.surface, (255,128,128), [x*10, y*10, 10, 10], 2)
        for b in self.bonus:
            b.draw()

    def checkCollision(self, ponto) -> bool:
        return ponto in self.walls
    
    def checkBonus(self, ponto) -> Bonus:
        for b in self.bonus:
            if ponto == b.position:
                return b
        return None
    
    def eatBonus(self, b):
        self.bonus.remove(b)

    def generateBonus(self):
        while True:
            x, y = random.randint(0,79), random.randint(0,59)
            if (x,y) not in self.walls:
                break
        self.bonus.append(Bonus(self.surface, x, y))

    def update(self):
        for b in self.bonus:
            b.update()
            if b.podre:
                self.bonus.remove(b)
                self.bonus.append(Bonus(self.surface, random.randint(1,78), random.randint(1,58)))
            
            