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


    def headGraphics(self):
        headRelation = self.body[1] - self.body[0]              #roznica miedzy 1 a 2 blokiem, aby ustalic kierunek weza

        if headRelation == Vector2(-1, 0):
            self.head = self.headRight                           #przypiosujemy do self.head dany obrazek
        elif headRelation == Vector2(1, 0):
            self.head = self.headLeft
        elif headRelation == Vector2(0, 1):
            self.head = self.headUp
        elif headRelation == Vector2(0, -1):
            self.head = self.headDown

    def tailGraphics(self):
        tailRelation = self.body[-2] - self.body[-1]              #roznica miedzy ostatnim a przedostartnim elementem weza

        if tailRelation == Vector2(-1, 0):
            self.tail = self.tailRight                           #przypiosujemy do self.head dany obrazek
        elif tailRelation == Vector2(1, 0):
            self.tail = self.tailLeft
        elif tailRelation == Vector2(0, 1):
            self.tail = self.tailUp
        elif tailRelation == Vector2(0, -1):
            self.tail = self.tailDown 



    def drawSnake(self):
        
        self.headGraphics()
        self.tailGraphics()

        for index, block in enumerate(self.body):             #dla kazdego blocku w indexach body (indexuje)  np. index 0 , block Vector2(5,10)
            snakeRect = pygame.Rect(block.x * cellSize, block.y * cellSize, cellSize, cellSize)  #potrzebujemy rect aby dac tam snakea

            if index == 0:                                    #glowa
                screen.blit(self.head, snakeRect)              #w zaleznosci od kierunku wyzej narysuje dany obrazek w snakeRect w bloku 0
            elif index == len(self.body) - 1:
                screen.blit(self.tail, snakeRect)           
            else:
                previousBlock = self.body[index +1] - block     #dostajemy vector z indexem jeden wyzej i demujmey current, aby byla roznica
                nextBlock = self.body[index - 1] - block          #vector z indexem jeden nizej i odejmujemy curent, aby byla roznica i kierunek
                if previousBlock.x == nextBlock.x:
                    screen.blit(self.bodyVertical, snakeRect)
                elif previousBlock.y == nextBlock.y:
                    screen.blit(self.bodyHorizontal, snakeRect)
                elif previousBlock.x == -1 and nextBlock.y == -1 or previousBlock.y == -1 and nextBlock.x == -1: #sprawdzamy jaka jest roznica miedzy wspolrzednymi poprzedniego, teraz i nastpengo bloku (narysuj sobie!!)
                    screen.blit(self.bodyTopLeft, snakeRect)
                elif previousBlock.x == -1 and nextBlock.y == 1 or previousBlock.y == 1 and nextBlock.x == -1:
                    screen.blit(self.bodyBottomLeft, snakeRect)
                elif previousBlock.x == 1 and nextBlock.y == -1 or previousBlock.y == -1 and nextBlock.x == 1:
                    screen.blit(self.bodyTopRight, snakeRect)
                elif previousBlock.x == 1 and nextBlock.y == 1 or previousBlock.y == 1 and nextBlock.x == 1:
                    screen.blit(self.bodyBottomRight, snakeRect)



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
