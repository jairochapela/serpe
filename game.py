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

        timer_interval = 500 # 0.5 seconds
        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event, timer_interval)
                
        while running:

            # Dibujar fondo y sprites
            self.field.draw()
            self.snake.draw()
            pygame.display.update()

            # Atender eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == timer_event:
                    print("tik")
                    self.snake.move()
