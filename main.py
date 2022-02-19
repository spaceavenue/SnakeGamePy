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
           self.y = random.randint(0, block_size - 1)
           self.pos = pyg.math.Vector2(self.x, self.y)

class Snake:
    def __init__(self):
        self.body = [pyg.math.Vector2(5, 10), pyg.math.Vector2(4, 10)]
        self.direction = pyg.math.Vector2(1, 0)
        self.add_new = False
        self.score_original = 0
        self.score_new = 0
        self.speed = 100

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

#    def scoreCount(self):
#        self.score_new += 1
#        print(self.score_new)

#    def gameSpeed(self):
#        match (self.score_new - self.score_original):
#                case 5:
#                        self.speed -= 10
#                        self.score_original = self.score_new
class Main:
    def __init__(self): 
        self.snake = Snake()
        self.fruit = Fruit()
#        self.SCREEN_UPDATE = pyg.USEREVENT
    def update(self):
#        SCREEN_UPDATE = pyg.USEREVENT
#        pyg.time.set_timer(self.SCREEN_UPDATE, self.snake.speed)
        self.snake.moveSnake()
        self.checkCollision()
        self.gameSpeed()
        self.checkGameOver()

    def drawStuff(self):
        self.fruit.drawFruit()
        self.snake.drawSnake()

    def checkCollision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.random()
            self.snake.addVec()
            self.snake.score_new += 1

    def gameSpeed(self):
        if self.snake.score_new - self.snake.score_original == 1:
            self.snake.speed -= 25
            self.snake.score_original = self.snake.score_new

    def checkGameOver(self):
        if not 0 <= self.snake.body[0].x <= block_num or not 0 <= self.snake.body[0].y <= block_num:
            self.gameOver()
        for snek in self.snake.body[1:]:
            if snek == self.snake.body[0]:
                self.gameOver()

    def gameOver():
        pyg.quit()

pyg.init()
block_num = 50
block_size = 10
window = pyg.display.set_mode((block_num * block_size, block_num * block_size))

mainGame = Main()
screen_update = pyg.USEREVENT
def thing(su, speed):
#    SCREEN_UPDATE = pyg.USEREVENT
    pyg.time.set_timer(su, speed)

while True:
    thing(screen_update, mainGame.snake.speed)
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
    pyg.display.update()
