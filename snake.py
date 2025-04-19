import pygame
from pygame.math import Vector2



cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellNumber *cellSize, cellNumber *cellSize))   
clock = pygame.time.Clock() 


class Snake:
    def __init__(self):    #to co sie stanie przy inicialization
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]  #tworzymy liste, ktora reprezentruje weza - nazwa body random
        self.movingDirection = Vector2(1, 0)
        self.newBlock = False

    def drawSnake(self):
        for block in self.body:     #dla kazddego blocku (nazwa random) w snaku (selfbody wyzej)
           snakeRect = pygame.Rect(block.x * cellSize, block.y * cellSize, cellSize, cellSize) #np dla 1 block bierzemy wspolrzedna x i aby byla kratka
           pygame.draw.rect(screen, (183, 111, 122), snakeRect)

    def moveSnake(self):
        if self.newBlock == True:
            bodyCopy = self.body[:]     #tworzymy copie snakea, ktora ma wszystkie elementy oprocz ostatniego
            bodyCopy.insert(0, bodyCopy[0] + self.movingDirection)   #dodajemy element do copii na samym poczatrku z kierunkiem insert
            self.body = bodyCopy
            self.newBlock = False
        else:
            bodyCopy = self.body[:-1]     #tworzymy copie snakea, ktora ma wszystkie elementy oprocz ostatniego
            bodyCopy.insert(0, bodyCopy[0] + self.movingDirection)   #dodajemy element do copii na samym poczatrku z kierunkiem insert
            self.body = bodyCopy

    def addBlock(self):
        self.newBlock = True
