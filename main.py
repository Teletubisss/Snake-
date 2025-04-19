import pygame
import sys
import random
from pygame.math import Vector2   #nie trzeba pisac za kazdym razem pygame.math
from snake import Snake
from fruit import Fruit





class Main:                     #mechanika gryu, aby bylo ladniej
    def __init__(self):
        self.snake = Snake()   #tworzymy obiekt snake o klasie snake 
        self.fruit = Fruit()

    def update(self):                     #gdy wywolamy funkcje update
        self.snake.moveSnake()   
        self.checkCollision()

    def drawElements(self):
        self.fruit.drawFruit()    #wywolujemy u obiektu fruit funkcje drawFruit
        self.snake.drawSnake()

    def checkCollision (self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.addBlock()




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