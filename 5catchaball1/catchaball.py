import pygame
import pygame
from pygame.draw import *
from random import randint
import math
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
N=10
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
t=0.1

def draw_new_ball():
    '''рисует новую партию двигающихся шариков'''
    global x, y, r, vx, vy,t,a,R,R0,V,n, color
    n=randint(2,N)
    x = [randint(R, a-R) for i in range(n)]
    y = [randint(R, a-R) for i in range(n)]
    vx = [randint(-V,V) for i in range(n)]
    vy = [randint(-V,V) for i in range(n)]
    r = [randint(R0, R) for i in range(n)]
    color = [COLORS[randint(0, 5)] for i in range(n)]
    g=0
    for i in range (n):
        circle(screen, color[g], (x[g], y[g]), r[g])
        g+=1
    pygame.display.update()
    for i in range (50):
        clock.tick(30)
        g=0
        for i in range(n):
            x[g] += vx[g]*t
            y[g] += vy[g]*t
            if (x[g]-r[g])<0:
                x[g]=r[g]
                vx[g]=-vx[g]
            elif (x[g]+r[g])>(a):
                vx[g]=-vx[g]
                x[g] = a-r[g]
            if (y[g]-r[g])<0:
                y[g]=r[g]
                vy[g]=-vy[g]
            elif (y[g]+r[g])>a:
                vy[g]=-vy[g]
                y[g] = a-r[g]
            g+=1
        g=0
        screen.fill(BLACK)
        for i in range (n):
            circle(screen, color[g], (x[g], y[g]), r[g])
            g+=1
        pygame.display.update()

def click_check():
    '''проверяет, попал ли щелчок мыши на какой-либо из шариков'''
    global eventx, eventy, scores, n 
    z=0
    eventx,eventy = pygame.mouse.get_pos()
    for i in range(n):
        d = (eventx-x[z])**2+(eventy-y[z])**2
        b = r[z]**2
        if d<=b:
            scores+=1
            print('Click! +1 score! scores:', scores)
            color[z]=BLACK
            pygame.display.update()
        z += 1
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_check()
    draw_new_ball()
    pygame.display.update()
    screen.fill(BLACK)
            

pygame.quit()

