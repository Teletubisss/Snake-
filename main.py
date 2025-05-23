import pygame
import sys
import random
from pygame.math import Vector2   #nie trzeba pisac za kazdym razem pygame.math
from snake import Snake
from fruit import Fruit


pygame.init()   

cellSize = 40
cellNumber = 20
apple = pygame.image.load('images/apple.png').convert_alpha()   #konwertuje aby bylo prosciej dla pygame
apple = pygame.transform.scale(apple, (cellSize, cellSize))
screen = pygame.display.set_mode((cellNumber *cellSize, cellNumber *cellSize))   


class Main:                     #mechanika gryu, aby bylo ladniej
    def __init__(self):
        self.snake = Snake()   #tworzymy obiekt snake o klasie snake 
        self.fruit = Fruit()

    def update(self):                     #gdy wywolamy funkcje update
        self.snake.moveSnake()   
        self.checkCollision()

    def drawElements(self):
        self.drawGrass()                    #bez obiektu, bo na sobie rysujemy
        self.fruit.drawFruit()    #wywolujemy u obiektu fruit funkcje drawFruit
        self.snake.drawSnake()
        self.drawScore()

    def checkCollision (self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.addBlock()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

        if not 0 <= self.snake.body[0].x < cellNumber or not 0<= self.snake.body[0].y <cellNumber:  #cellNu - * przez cellSi przy rysowaniu > screen
            self.gameOver()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.gameOver()

    def gameOver(self):
        self.snake.reset() 

    def drawGrass(self):
        grassColor = (167, 209, 61)
        for row in range(cellNumber):
            if row % 2 == 0:
                for col in range(cellNumber):
                    if col % 2 == 0:                                           #parzyste
                        grassRect = pygame.Rect(col * cellSize ,row * cellSize,cellSize, cellSize)  #znajduje sie w danej kol (mnozymy przez cS, aby byla siatka)
                        pygame.draw.rect(screen, grassColor, grassRect)
            else:
                for col in range(cellNumber):
                    if col % 2 != 0:                                           #nieparzyste
                        grassRect = pygame.Rect(col * cellSize ,row * cellSize,cellSize, cellSize)  #znajduje sie w danej kol (mnozymy przez cS, aby byla siatka)
                        pygame.draw.rect(screen, grassColor, grassRect)

    def drawScore(self):
        scoreText = str(len(self.snake.body) - 3)
        scoreSurface = gameFont.render(scoreText, True, (56,74,12))  #tworzymy grafika z napisem (mp surface z "hejka") - (tekst, wygladzanie, kolor)
        scoreX = cellSize*cellNumber - 60
        scoreY = cellSize*cellNumber - 40
        scoreRect = scoreSurface.get_rect(center = (scoreX, scoreY))  #ustawiamy środek (center) na jakies x,y. Rect obliocza rozmiar obrazu i ustawia
        appleRect = apple.get_rect(midright = (scoreRect.left, scoreRect.centery))

        bgRect = pygame.Rect(appleRect.left, appleRect.top, appleRect.width + scoreRect.width + 6, appleRect.height + 3)
        pygame.draw.rect(screen, (167, 209, 161), bgRect)
        pygame.draw.rect(screen, (56,74,12), bgRect, 2)
        screen.blit(apple, appleRect)
        screen.blit(scoreSurface, scoreRect)



pygame.init() 
clock = pygame.time.Clock() 
gameFont = pygame.font.Font('fonts/StardewValley.ttf', 25)                        



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
                if mainGame.snake.movingDirection.y !=1: 
                    mainGame.snake.movingDirection = Vector2(0, -1)          #zmieniamy movingdirection na do gory 
            if event.key == pygame.K_DOWN:   
                if mainGame.snake.movingDirection.y !=-1:  
                    mainGame.snake.movingDirection = Vector2(0, 1)
            if event.key == pygame.K_LEFT: 
                if mainGame.snake.movingDirection.x !=1:    
                    mainGame.snake.movingDirection = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:    
                if mainGame.snake.movingDirection.x !=-1: 
                    mainGame.snake.movingDirection = Vector2(1, 0)
                 

    screen.fill((167, 209, 121))   #fillujemy screen kolorem

    mainGame.drawElements()

    pygame.display.update()                     
    clock.tick(60)                             