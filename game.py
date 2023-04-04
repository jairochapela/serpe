import pygame
from snake import Snake
from field import Field




class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.field = Field(self.window)
        self.snake = Snake(self.window)
        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        self.keymapping = {
            pygame.K_LEFT: lambda : self.snake.changeDirection((-1, 0)),
            pygame.K_RIGHT: lambda : self.snake.changeDirection((1, 0)),
            pygame.K_UP: lambda : self.snake.changeDirection((0, -1)),
            pygame.K_DOWN: lambda : self.snake.changeDirection((0, 1)),
        }
        self.timer_interval = 125 # 0.125 seconds
        self.timer_event = pygame.USEREVENT + 1    
        self.showScore = 0      


    def increaseScore(self, n):
        self.score += n
        self.showScore = 1000


    def draw(self):
        # Dibujar fondo y sprites
        self.field.draw()
        self.snake.draw()
        if self.showScore > 0:
            text_surface = self.font.render(f"{self.score}", False, (255, 255, 255))
            self.window.blit(text_surface, (20, 20))
            self.showScore -= 1


    def processEvents(self):              
        # Atender eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                for k,f in self.keymapping.items():
                    if event.key == k: f()
            elif event.type == self.timer_event:
                self.snake.move()
                self.field.update()


    def update(self):
        #Cálculos
        if self.field.checkCollision(self.snake.head):
            print("BOOM")
            self.running = False
        if self.snake.checkCollision():
            self.running = False

        b = self.field.checkBonus(self.snake.head)
        if b:
            print("BONUS")
            self.field.eatBonus(b)
            self.snake.grow(3)
            self.field.generateBonus()
            self.increaseScore(1)

    def start(self):
        self.running = True
        pygame.time.set_timer(self.timer_event, self.timer_interval)
                
        self.score = 0

        while self.running:
            self.draw()
            pygame.display.update()

            self.processEvents()
            self.update()

