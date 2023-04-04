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

        timer_interval = 125 # 0.125 seconds
        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event, timer_interval)
                
        keymapping = {
            pygame.K_LEFT: lambda : self.snake.changeDirection((-1, 0)),
            pygame.K_RIGHT: lambda : self.snake.changeDirection((1, 0)),
            pygame.K_UP: lambda : self.snake.changeDirection((0, -1)),
            pygame.K_DOWN: lambda : self.snake.changeDirection((0, 1)),
        }

        while running:
            #Cálculos
            if self.field.checkCollision(self.snake.head):
                print("BOOM")
                running = False
            if self.snake.checkCollision():
                running = False

            b = self.field.checkBonus(self.snake.head)
            if b:
                print("BONUS")
                self.field.eatBonus(b)
                self.snake.grow(3)
                self.field.generateBonus()

            # Dibujar fondo y sprites
            self.field.draw()
            self.snake.draw()
            pygame.display.update()

            # Atender eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    for k,f in keymapping.items():
                        if event.key == k: f()
                elif event.type == timer_event:
                    self.snake.move()
                    self.field.update()
