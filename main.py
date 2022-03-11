import pygame as pyg 
import random 

class Fruit:
    def __init__(self):
        self.x = random.randint(0, block_num - 1)
        self.y = random.randint(0, block_size - 1)
        self.pos = pyg.math.Vector2(self.x, self.y)

    def drawFruit(self):
        fruit = pyg.Rect(self.pos.x * block_size, self.pos.y * block_size, block_size, block_size)
        pyg.draw.rect(window, (255, 0, 0), fruit)

    def random(self):
           self.x = random.randint(0, block_num - 1)
           self.y = random.randint(0, block_num - 1)
           self.pos = pyg.math.Vector2(self.x, self.y)

class Snake:
    def __init__(self):
        self.body = [pyg.math.Vector2(5, 10), pyg.math.Vector2(4, 10)]
        self.direction = pyg.math.Vector2(1, 0)
        self.add_new = False
        self.score = 0

    def drawSnake(self):
        for vec in self.body:
            snake = pyg.Rect(vec.x * block_size, vec.y * block_size, block_size, block_size)
            pyg.draw.rect(window, (0, 255, 0), snake)

    def moveSnake(self):
        if self.add_new == True: 
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.add_new = False

        else: 
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            
    def addVec(self):
        self.add_new = True

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.font = pyg.font.SysFont("Arial", 14, bold=True, italic=False)

    def update(self):
        self.snake.moveSnake()
        self.checkCollision()
        self.checkGameOver()

    def drawStuff(self):
        self.fruit.drawFruit()
        self.snake.drawSnake()
        self.font_surface = self.font.render(str(self.snake.score), False, (255,255,255))

    def checkCollision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.random()
            self.snake.addVec()
            self.snake.score += 1

    def checkGameOver(self):
        if not 0 <= self.snake.body[0].x <= block_num or not 0 <= self.snake.body[0].y <= block_num:
            raise "what"
            
        for snek in self.snake.body[1:]:
            if snek == self.snake.body[0]:
                raise "what"
    

    def gameOver(self):
        window.fill((0,0,0))
        self.font = pyg.font.SysFont("Arial", 32, bold=True, italic=False)
        self.death_message = self.font.render("You Died.", False, (255,255,255))
        window.blit(self.death_message, (125, 125))
        self.replay_input = self.font.render("Press Enter to play again, Esape to quit.", False, (255,255,255))
        window.blit(self.replay_input, (150, 150))
        pyg.display.update()

pyg.init()
block_num = 50
block_size = 10
window = pyg.display.set_mode((block_num * block_size, block_num * block_size))
gameover_window = pyg.display.set_mode((block_num * block_size, block_num * block_size))

mainGame = Main()
SCREEN_UPDATE = pyg.USEREVENT
pyg.time.set_timer(SCREEN_UPDATE, 50)
running = True

try:
    while running:
    
        for event in pyg.event.get():

            if event.type == pyg.QUIT:
                pyg.quit()

            elif event.type == SCREEN_UPDATE:
                mainGame.update()

            elif event.type == pyg.KEYDOWN:
                match event.key:
                    case pyg.K_UP:
                        if mainGame.snake.direction.y != 1:
                            mainGame.snake.direction = pyg.math.Vector2(0, -1)
                    case pyg.K_DOWN:
                        if mainGame.snake.direction.y != -1:
                            mainGame.snake.direction = pyg.math.Vector2(0, 1)
                    case pyg.K_LEFT:
                        if mainGame.snake.direction.x != 1:
                            mainGame.snake.direction = pyg.math.Vector2(-1, 0)
                    case pyg.K_RIGHT:
                        if mainGame.snake.direction.x != -1:
                            mainGame.snake.direction = pyg.math.Vector2(1, 0)
                    case pyg.K_ESCAPE:
                        pyg.quit()
        
        window.fill((0, 0, 0))
        mainGame.drawStuff()
        window.blit(mainGame.font_surface, (5,5))
        pyg.display.update()

except Exception as e:
    while True:
        for event in pyg.event.get():
            if event.type == SCREEN_UPDATE:
                mainGame.gameOver()
            elif event.type == pyg.KEYDOWN:
                match event.key:
                    case pyg.K_RETURN:
                        mainGame.__init__()
                    case pyg.K_ESCAPE:
                        pyg.quit()