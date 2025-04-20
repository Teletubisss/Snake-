import pygame
from pygame.math import Vector2
import random


cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellNumber *cellSize, cellNumber *cellSize))   
clock = pygame.time.Clock() 
apple = pygame.image.load('images/apple.png').convert_alpha()   #konwertuje aby bylo prosciej dla pygame
apple = pygame.transform.scale(apple, (cellSize, cellSize))

class Fruit:
    def __init__(self):
        self.randomize()

    def drawFruit(self):
        fruitRect = pygame.Rect(self.pos.x * cellSize, self.pos.y * cellSize, cellSize, cellSize) #mnozymy, aby byla git grafika
        screen.blit(apple, fruitRect)                    #co chcemy narysowac i gdzie chcemy narusowac

    def randomize(self):
        self.x = random.randint(0, cellNumber - 1) #byloby za ekranem - obiekt od lewego gornego rogu  - nazwa x random
        self.y = random.randint(0, cellNumber - 1)    #nazwa y random dla obiektu w obiekcie o tej klasie
        self.pos = Vector2(self.x, self.y)    #uzywamy vectorow, bo prosciej bedzie je zmieniac np o 2 w prawo. moznaby lista - l = [5,4]