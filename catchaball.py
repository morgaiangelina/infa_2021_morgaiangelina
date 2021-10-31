import pygame
import pygame
from pygame.draw import *
from random import randint
import math
pygame.init()

FPS = 1

scores=0
#количество очков
a=500
#длина стороны окна
R=50 #максимальный радиус шариков
R0=10 #минимальный радиус шариков
V=100 #максимальная скорость шариков
screen = pygame.display.set_mode((a, a))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
t=0.1

def draw_new_ball():
    '''рисует новый двигающийся шарик шарик'''
    global x, y, r, vx, vy,t,a,R,R0,V
    vx = randint(-V,V)
    vy = randint(-V,V)
    x = randint(R, a-R)
    y = randint(R, a-R)
    r = randint(R0, R)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    pygame.display.update()
    for i in range(20):
        clock.tick(30)
        screen.fill(BLACK)
        x += vx*t
        y += vy*t
        if (x-r)<0:
            x=r
            vx=-vx
        elif (x+r)>(a):
            vx=-vx
            x = a-r
        if (y-r)<0:
            y=r
            vy=-vy
        elif (y+r)>a:
            vy=-vy
            y = 900-r
        circle(screen, color, (x, y), r)
        pygame.display.update()
        
def click_check():
    '''проверяет, попал ли щелчок мыши на шарик'''
    global eventx, eventy, scores
    eventx,eventy = pygame.mouse.get_pos()
    eventx=int(eventx)
    eventy=int(eventy)
    a = (eventx-x)**2+(eventy-y)**2
    b = (r**2)
    if a<=b:
        clock.tick(30)
        scores+=1
        print('Click! +1 score! scores:', scores)
        screen.fill(BLACK)
        pygame.display.update()
    elif a>(b):
        print('Missed click!')
        
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_check()
    draw_new_ball()
    pygame.display.update()
    screen.fill(BLACK)
            

pygame.quit()
