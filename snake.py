import pygame
from pygame.math import Vector2



cellSize = 40
cellNumber = 20
screen = pygame.display.set_mode((cellNumber *cellSize, cellNumber *cellSize))   
clock = pygame.time.Clock() 


class Snake:
    def __init__(self):    #to co sie stanie przy inicialization
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]  #tworzymy liste, ktora reprezentruje weza - nazwa body random
        self.movingDirection = Vector2(1, 0)
        self.newBlock = False

        self.headUp = pygame.image.load('images/head_up.png').convert_alpha()
        self.headDown = pygame.image.load('images/head_down.png').convert_alpha()
        self.headLeft = pygame.image.load('images/head_left.png').convert_alpha()
        self.headRight = pygame.image.load('images/head_right.png').convert_alpha()
        self.tailUp = pygame.image.load('images/tail_up.png').convert_alpha()
        self.tailDown = pygame.image.load('images/tail_down.png').convert_alpha()
        self.tailLeft = pygame.image.load('images/tail_left.png').convert_alpha()
        self.tailRight = pygame.image.load('images/tail_right.png').convert_alpha()
        self.bodyVertical = pygame.image.load('images/body_vertical.png').convert_alpha()
        self.bodyHorizontal = pygame.image.load('images/body_horizontal.png').convert_alpha()
        self.bodyTopLeft = pygame.image.load('images/body_topleft.png').convert_alpha()
        self.bodyTopRight = pygame.image.load('images/body_topright.png').convert_alpha()
        self.bodyBottomLeft = pygame.image.load('images/body_bottomleft.png').convert_alpha()
        self.bodyBottomRight = pygame.image.load('images/body_bottomright.png').convert_alpha()

    def drawSnake(self):

        for index, block in enumerate(self.body):             #dla kazdego blocku w indexach body (indexuje)  np. index 0 , block Vector2(5,10)
            snakeRect = pygame.Rect(block.x * cellSize, block.y * cellSize, cellSize, cellSize)  #potrzebujem,y rect aby dac tam snakea

            if index == 0:                        #glowa
                screen.blit(self.headRight, snakeRect)
            else:
                pygame,.draw.rect(screen, (150, 100, 100), snakeRect)

    def moveSnake(self):
        if self.newBlock == True:
            self.moveOrEat(None)
            self.newBlock = False
        else:
            self.moveOrEat(-1)
    
    
    def moveOrEat(self, index):
        if index is None:
            bodyCopy = self.body[:]  #tworzymy copie snakea, ktora ma wszystkie elementy 
        else:
            bodyCopy = self.body[:index]  # kopiujemy bez ostatniego elementu

        bodyCopy.insert(0, bodyCopy[0] + self.movingDirection) #dodajemy element do copii na samym poczatrku z kierunkiem insert (miejwsce, element)
        self.body = bodyCopy


    def addBlock(self):
        self.newBlock = True
