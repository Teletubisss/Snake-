import pygame
import sys
import random
from pygame.math import Vector2   #nie trzeba pisac za kazdym razem pygame.math



class Snake:
    def __init__(self):    #to co sie stanie przy inicialization
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]  #tworzymy liste, ktora reprezentruje weza - nazwa body random
        self.movingDirection = Vector2(1, 0)

    def drawSnake(self):
        for block in self.body:     #dla kazddego blocku (nazwa random) w snaku (selfbody wyzej)
           snakeRect = pygame.Rect(block.x * cellSize, block.y * cellSize, cellSize, cellSize) #np dla 1 block bierzemy wspolrzedna x i aby byla kratka
           pygame.draw.rect(screen, (183, 111, 122), snakeRect)

    def moveSnake(self):
        bodyCopy = self.body[:-1]     #tworzymy copie snakea, ktora ma wszystkie elementy oprocz ostatniego
        bodyCopy.insert(0, bodyCopy[0] + self.movingDirection)   #dodajemy element do copii na samym poczatrku z kierunkiem insert
        self.body = bodyCopy



class Fruit:
    def __init__(self):
        self.x = random.randint(0, cellNumber - 1) #byloby za ekranem - obiekt od lewego gornego rogu  - nazwa x random
        self.y = random.randint(0, cellNumber - 1)    #nazwa y random dla obiektu w obiekcie o tej klasie
        self.pos = Vector2(self.x, self.y)    #uzywamy vectorow, bo prosciej bedzie je zmieniac np o 2 w prawo. moznaby lista - l = [5,4]

    def drawFruit(self):
        fruitRect = pygame.Rect(self.pos.x * cellSize, self.pos.y * cellSize, cellSize, cellSize) #mnozymy, aby byla git grafika
        pygame.draw.rect(screen, (126, 166, 114), fruitRect)


class Main:                     #mechanika gryu, aby bylo ladniej
    def __init__(self):
        self.snake = Snake()   #tworzymy obiekt snake o klasie snake 
        self.fruit = Fruit()

    def update(self):                     #gdy wywolamy funkcje update
        self.snake.moveSnake()   

    def drawElements(self):
        self.fruit.drawFruit()    #wywolujemy u obiektu fruit funkcje drawFruit
        self.snake.drawSnake()


pygame.init()                               

cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellNumber *cellSize, cellNumber *cellSize))   
clock = pygame.time.Clock() 

screenUpdate = pygame.USEREVENT  #wlasny event (jeszcze nie wiemy jaki)mamy do wykorzystania 9 eventow, to jest pierwszy - nastepny to userevent + 1
pygame.time.set_timer(screenUpdate, 150)         #ustawiamy timer i wysyla sie tik co 150 milisekund w formie userevent         



mainGame = Main()


while True:                                 
    for event in pygame.event.get():          #sprawdza wszystkie zdarzenia, ktore sie wydarzyly (np. klikniecie, timer)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    

        if event.type == screenUpdate:   #jezeli event to bedzie ten wyslany tik z screenUpdate
            mainGame.update()
        if event.type == pygame.KEYDOWN:    #dla kazdego nacisnietego klawisza
            if event.key == pygame.K_UP:    
                mainGame.snake.movingDirection = Vector2(0, -1)          #zmieniamy movingdirection na do gory 
            if event.key == pygame.K_DOWN:    
                mainGame.snake.movingDirection = Vector2(0, 1)
            if event.key == pygame.K_LEFT:    
                mainGame.snake.movingDirection = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:    
                mainGame.snake.movingDirection = Vector2(1, 0)
                 

    screen.fill((75, 180, 113))   #fillujemy screen kolorem

    mainGame.drawElements()

    pygame.display.update()                     
    clock.tick(60)                             