import pygame as pyg 
import random 

#exception class for snake collision with self and walls
class what(Exception):
    pass

class Fruit:
    
    #set fruit pos vectors
    def __init__(self):
        self.x = random.randint(0, block_num - 1)
        self.y = random.randint(0, block_size - 1)
        self.pos = pyg.math.Vector2(self.x, self.y)

    #draw the fruit
    def drawFruit(self):
        fruit = pyg.Rect(self.pos.x * block_size, self.pos.y * block_size, block_size, block_size)
        pyg.draw.rect(window, (255, 0, 0), fruit)
    
    #randomise next fruit spawn location
    def random(self):
           self.x = random.randint(0, block_num - 1)
           self.y = random.randint(0, block_num - 1)
           self.pos = pyg.math.Vector2(self.x, self.y)

class Snake:
    
    #add initial snake size, direction of snake movement and score
    def __init__(self):
        self.body = [pyg.math.Vector2(5, 10), pyg.math.Vector2(4, 10)]
        self.direction = pyg.math.Vector2(1, 0)
        self.add_new = False
        self.score = 0

    #draw the snake
    def drawSnake(self):
        for vec in self.body:
            snake = pyg.Rect(vec.x * block_size, vec.y * block_size, block_size, block_size)
            pyg.draw.rect(window, (0, 255, 0), snake)

    #add snake movement mechanic
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

        self.drawSnake()

    #set variable for extending snake
    def addVec(self):
        self.add_new = True

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.font = pyg.font.SysFont("Arial", 14, bold=True, italic=False)

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
        for i in range(25):
            if not 0 <= self.snake.body[0].x <= block_num or not 0 <= self.snake.body[0].y <= block_num:
                flag = True
            else:
                flag = False
            return flag

        else:
            for snake_part in self.snake.body[1:]:
                if snake_part == self.snake.body[0]:
                    flag = True
                else:
                    flag = False
            return flag
    
    def update(self):
        self.snake.moveSnake()
        self.checkCollision()
        self.checkGameOver()
        self.drawStuff()
        pyg.display.update()

    def gameOver(self):
        window.fill((0,0,0))
        self.font = pyg.font.SysFont("Arial", 32, bold=True, italic=False)
        self.death_message = self.font.render("You Died.", False, (255,255,255))
        window.blit(self.death_message, (125, 125))
        self.replay_input = self.font.render("Press Enter to play again, Esape to quit.", False, (255,255,255))
        window.blit(self.replay_input, (150, 150))
        pyg.display.update()

    def runner(self):
        while True:
            if self.checkGameOver() == True:
                self.gameOver()
                for event in pyg.event.get():
                    if event.type == pyg.KEYDOWN:
                        match event.key:
                            case pyg.K_RETURN:
                                self.__init__()
                                self.runner()
                            case pyg.K_ESCAPE:
                                pyg.quit()
            else:
                for event in pyg.event.get():
                    if event.type == pyg.QUIT:
                        pyg.quit()

                    elif event.type == SCREEN_UPDATE:
                        self.update()

                    elif event.type == pyg.KEYDOWN:
                        match event.key:
                            case pyg.K_UP:
                                if self.snake.direction.y != 1:
                                    self.snake.direction = pyg.math.Vector2(0, -1)
                            case pyg.K_DOWN:
                                if self.snake.direction.y != -1:
                                    self.snake.direction = pyg.math.Vector2(0, 1)
                            case pyg.K_LEFT:
                                if self.snake.direction.x != 1:
                                    self.snake.direction = pyg.math.Vector2(-1, 0)
                            case pyg.K_RIGHT:
                                if self.snake.direction.x != -1:
                                    self.snake.direction = pyg.math.Vector2(1, 0)
                            case pyg.K_ESCAPE:
                                pyg.quit()

            window.fill((0, 0, 0))
            self.drawStuff()
            window.blit(self.font_surface, (5,5))

pyg.init()
block_num = 50
block_size = 10
window = pyg.display.set_mode((block_num * block_size, block_num * block_size))
mainGame = Main()

SCREEN_UPDATE = pyg.USEREVENT
pyg.time.set_timer(SCREEN_UPDATE, 50)
mainGame.runner()
