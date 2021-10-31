import pygame
import pygame
from pygame.draw import *
from random import randint
import math
pygame.init()

FPS = 1

scores=0

screen = pygame.display.set_mode((900, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def draw_new_ball():
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100, 900)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
def click_check():
    '''проверяет, попал ли щелчок мышки на шарик'''
    global eventx, eventy, scores
    eventx,eventy = pygame.mouse.get_pos()
    eventx=int(eventx)
    eventy=int(eventy)
    a = (eventx-x)**2+(eventy-y)**2
    b = (r**2)
    if a<=b:
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
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_check()
    draw_new_ball()
    pygame.display.update()
    screen.fill(BLACK)
            

pygame.quit()
