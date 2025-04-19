import pygame
from pygame.math import Vector2
import random


cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellNumber *cellSize, cellNumber *cellSize))   
clock = pygame.time.Clock() 


class Fruit:
    def __init__(self):
        self.randomize()

    def drawFruit(self):
        fruitRect = pygame.Rect(self.pos.x * cellSize, self.pos.y * cellSize, cellSize, cellSize) #mnozymy, aby byla git grafika
        pygame.draw.rect(screen, (126, 166, 114), fruitRect)

    def randomize(self):
        self.x = random.randint(0, cellNumber - 1) #byloby za ekranem - obiekt od lewego gornego rogu  - nazwa x random
        self.y = random.randint(0, cellNumber - 1)    #nazwa y random dla obiektu w obiekcie o tej klasie
        self.pos = Vector2(self.x, self.y)    #uzywamy vectorow, bo prosciej bedzie je zmieniac np o 2 w prawo. moznaby lista - l = [5,4]