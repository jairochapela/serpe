import pygame
from snake import Snake
from field import Field

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.field = Field(self.window)
        self.snake = Snake(self.window)

    def start(self):
        running = True
        while running:

            # Dibujar fondo y sprites
            self.field.draw()
            self.snake.draw()
            pygame.display.update()
                        
            # Atender eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
