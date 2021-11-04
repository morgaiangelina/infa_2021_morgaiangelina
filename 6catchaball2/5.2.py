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

FPS = 30

scores=0
#количество очков
a=500
#длина стороны окна
R=50 #максимальный радиус шариков
R0=10 #минимальный радиус шариков
V=100 #максимальная скорость шариков
screen = pygame.display.set_mode((a, a))

w=0 
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


def draw_balls_and_donuts():
    '''рисует новую партию двигающихся шариков и пончиков'''
    global x, y, r, vx, vy,t,a,R,R0,V,x1, y1, r1, vx1, vy1, color, color1,n
    n=randint(2,N)
    x = [randint(R, a-R) for i in range(n)] # массив координат шариков по горизонтали
    y = [randint(R, a-R) for i in range(n)] # массив координат шариков по вертикали
    vx = [randint(-V,V) for i in range(n)] # массив горизонтальных скоростей шариков
    vy = [randint(-V,V) for i in range(n)] # массив вертикальных скоростей шариков
    r = [randint(R0, R) for i in range(n)] # массив радиусов шариков
    color = [COLORS[randint(0, 5)] for i in range(n)] # массив цветов шариков
    x1 = [randint(R, a-R) for i in range(n)] # массив координат пончиков по горизонтали
    y1 = [randint(R, a-R) for i in range(n)] # массив координат пончиков по вертикали
    vx1 = [randint(-V,V) for i in range(n)] # массив горизонтальных скоростей пончиков
    vy1 = [randint(-V,V) for i in range(n)] # массив вертикальных скоростей пончиков
    r1 = [randint(R0, R/2) for i in range(n)] # массив радиусов пончиков
    color1 = [COLORS[randint(0, 5)] for i in range(n)] # массив цветов пончиков
    g=0
    for i in range (n):
        circle(screen, color1[g], (x1[g], y1[g]), r1[g], round(r1[g]/2))
        circle(screen, color[g], (x[g], y[g]), r[g])
        g+=1
    pygame.display.update()


def move_balls_and_donuts():
    '''двигает партию двигающихся шариков и пончиков'''
    for g in range(n):
        x[g] += vx[g]*t
        y[g] += vy[g]*t
        x1[g] += randint(-V,V)*3*t
        y1[g] += randint(-V,V)*3*t
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
        if (x1[g]-r1[g])<0:
            x1[g]=r1[g]
        elif (x1[g]+r1[g])>(a):
            x1[g] = a-r1[g]
        if (y1[g]-r1[g])<0:
            y1[g]=r1[g]
        elif (y1[g]+r1[g])>a:
            y1[g] = a-r1[g]
    screen.fill(BLACK)
    for g in range (n):
        circle(screen, color1[g], (x1[g], y1[g]), r1[g], round(r1[g]/2))
        circle(screen, color[g], (x[g], y[g]), r[g])
    pygame.display.update()

def click_check():
    '''проверяет, попал ли щелчок мыши на какой-либо из шариков или пончиков'''
    global eventx, eventy, scores, n,w 
    eventx,eventy = pygame.mouse.get_pos()
    for i in range(n):
        d = (eventx-x[i])**2+(eventy-y[i])**2
        b = r[i]**2
        d1 = (eventx-x1[i])**2+(eventy-y1[i])**2
        b1 = r1[i]**2
        c1 = (r1[i]**2)/4
        if d<=b:
            scores+=1
            w+=1
            print('A ball is catched! +1 score! scores:', scores)
            x[i] = randint(R, a-R)
            y[i] = randint(R, a-R)
            vx[i] = randint(-V,V)
            vy[i] = randint(-V,V)
            r[i] = randint(R0, R)
            color[i] = COLORS[randint(0, 5)]
        if d1<=b1:
            if d1>=c1:
                scores+=5
                w+=5
                print('A donut is catched! +5 score! scores:', scores)
                x1[i] = randint(R, a-R)
                y1[i] = randint(R, a-R)
                vx1[i] = randint(-V,V)
                vy1[i] = randint(-V,V)
                r1[i] = randint(R0, R)
                color1[i] = COLORS[randint(0, 5)]

def save_scores():
    '''создаёт файл с упорядоченным набором очков игроков'''
    global finished
    f = open('scores.txt','a')
    f.write(name_of_player+'\n')
    f.write(str(scores)+'\n')
    f.close()
    j=0
    SCORES = []
    NAMES = []
    f = open('scores.txt','r')
    while True:
        line = f.readline()
        if not line:
            break
        if (-1)**j==1:
            DATA0 = str(line)
            DATA0.replace('\n','')
            NAMES.append(DATA0)
        elif (-1)**j==-1:
            DATA = str(line)
            DATA.replace('\n','')
            DATA = int(DATA)
            SCORES.append(DATA)
        j+=1                
    f.close()
    f = open('scores.txt','w')
    while max(SCORES)>-1:
        f.write(NAMES[SCORES.index(max(SCORES))])
        f.write(str(SCORES[SCORES.index(max(SCORES))])+'\n')
        SCORES[SCORES.index(max(SCORES))]=-1
    f.close()
    finished = True
        
pygame.display.update()
clock = pygame.time.Clock()
finished = False


print('Введите имя игрока:')
name_of_player = input()
draw_balls_and_donuts()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_scores()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_check()
    if w>=10:
        draw_balls_and_donuts()
        w=0
    move_balls_and_donuts()        
    pygame.display.update()


pygame.quit()

