import pygame
import sys


pygame.init()                                 #rozpoczyna pygame


screen = pygame.display.set_mode((400,500))   #tworzymy display surface - canvas, only one, display default 
clock = pygame.time.Clock()                   #modul do monitorowania czau, .Clock() - wytwarza objekt do mierzenia czasuu
test_surface = pygame.Surface((100,200))        #stworzylismy surface - 1 krok stworzenie, ale jeszcze nie dalismy go na ekrrn, wiec nie widac
test_rect = pygame.Rect(100, 200, 100, 100)
surface_pos = test_surface.get_rect(center = (200, 250))             #rysuje rect dookola, center- gdzie chchemy dac


while True:                                   #bedzie caly czas prawdziwa, dopoki nie zatrzymamy jej od srodka - bedziemy tutaj rysowac to, co bedzie na ekranie
    for event in pygame.event.get():          #pygame.event - interaktujer z eventami, .get() - bierze eventy z kolejki
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()                        #gdyby to na gorze sie rypnelo, to reszte wylaczy

    screen.fill((75, 180, 113))
    test_surface.fill((232, 100, 23))

    surface_pos.right += 1
    screen.blit(test_surface, surface_pos)      #screen.blit - na diusplay surface wrzuca i rysuje/blokuje test_surface - pozycja lewej gornej krawedzi

    pygame.draw.rect(screen, pygame.Color('red'), test_rect)  #rysuje rect (na czym, jaki kolor, jaki rect)

    pygame.display.update()                     #wrzxuca na ekran to, co my rysujem,y na tzw. sufrace - buforze ekranu
    clock.tick(60)                             #liczy czas co 60fps - gdyby nie to to na roznych kompach lecialoby szybciej lub woniei