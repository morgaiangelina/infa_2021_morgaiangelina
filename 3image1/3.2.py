import pygame
import random
from random import randint
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((550, 778))
WHITE =(255,255,255)
BLACK = (0,0,0)
YELLOW = (255,204,0)
rect(screen, (25,25,112), (0,0, 550, 71))
rect(screen, (123, 104, 238), (0,71, 550, 36))
rect(screen, (238,130,238), (0,107, 550, 70))
rect(screen, (219,112,147), (0,177, 550, 106))
rect(screen, (255, 127, 80), (0,283, 550, 106))
rect(screen, (32,178,170), (0,389, 550, 389))
e=-60
f=-30

def fish(x,y,h): #функция для рисования рыбы
    fish = pygame.Surface([1000,1000], pygame.SRCALPHA, 32)
    fish = fish.convert_alpha()
    polygon(fish, (25,25,112), [[0,2*h],[h,3*h],[0,4*h]])
    polygon(fish, BLACK, [[0,2*h],[h,3*h],[0,4*h]],1)
    polygon(fish, (25,25,112), [[3*h,3*h],[3*h,0],[4*h,3*h]])
    polygon(fish, BLACK, [[3*h,3*h],[3*h,0],[4*h,3*h]],1)
    polygon(fish, (25,25,112), [[3*h,5*h],[4*h,3*h],[3*h,3*h]])
    polygon(fish, BLACK, [[3*h,5*h],[4*h,3*h],[3*h,3*h]])
    ellipse(fish, (123, 104, 238), (h,2*h,4*h,2*h))
    ellipse(fish, BLACK, (h,2*h,4*h,2*h),1)
    ellipse(fish, (0,0,255), (4*h,2.5*h,0.6*h,0.6*h))
    ellipse(fish, (0,0,0), (4*h,2.5*h,0.6*h,0.6*h),1)
    ellipse(fish, BLACK, (4.2*h,2.5*h,0.3*h,0.3*h))
    line(fish,BLACK,[4*h,3.5*h],[4.7*h,3.5*h],1)
    screen.blit(fish,(x,y))
def smallbird(name,x,y,n,angle): #функция для рисования чайки
    name = pygame.Surface([640,480], pygame.SRCALPHA, 32)
    name = name.convert_alpha()
    arc(name,WHITE,(0,0,4*n,3*n),0, 2.7, 3)
    arc(name,WHITE,(4*n,0,4*n,3*n),0.75, 3.14, 3)
    name = pygame.transform.rotate(name, angle)
    screen.blit(name,(x,y))
smallbird('1',20,200,20,-12)
smallbird('1',40,140,10,-12)
smallbird('2',20,10,15,12)
smallbird('3',27,70,10,-19)
smallbird('2',10,-50,11,12)
smallbird('1',0,200,20,12)
smallbird('1',0,150,10,6)
smallbird('1',20,250,10,-6)
smallbird('1',50,320,15,-12)
smallbird('1',220,330,15,-12)

smallbird('1',e+320,f+200,20,-12)
smallbird('1',e+340,f+140,10,-12)
smallbird('2',e+320,f+10,15,12)
smallbird('3',e+327,f+70,10,-19)
smallbird('2',e+310,f+-50,11,12)
smallbird('1',e+300,f+200,20,12)
smallbird('1',e+300,f+150,10,6)
smallbird('1',e+320,f+250,10,-6)
smallbird('1',e+350,f+320,15,-12)

firstbigbird = pygame.Surface([550,778], pygame.SRCALPHA, 32)
firstbigbird = firstbigbird.convert_alpha()

polygon(firstbigbird, WHITE, [[200,590],[150,550],[140,600],[190,600]]) #хвост
wig1 = pygame.Surface([400,400], pygame.SRCALPHA, 32) #крыло 1
wig1 = wig1.convert_alpha()
polygon(wig1, WHITE, [[200,200],[200,155],[170,85],[85,60],[105,80],[90,80],[110,100],[95,100],[115,120],[100,120],[120,140],[105,140],[125,160],[110,160],[130,180],[115,180],[160,200]])
polygon(wig1, BLACK, [[200,200],[200,155],[170,85],[85,60],[105,80],[90,80],[110,100],[95,100],[115,120],[100,120],[120,140],[105,140],[125,160],[110,160],[130,180],[115,180],[160,200]],1)
wig1 = pygame.transform.rotate(wig1, 0)
firstbigbird.blit(wig1,(140,380)) 



wig2 = pygame.Surface([400,400], pygame.SRCALPHA, 32)
wig2 = wig2.convert_alpha()
polygon(wig2, WHITE, [[200,200],[200,155],[170,85],[85,60],[105,80],[90,80],[110,100],[95,100],[115,120],[100,120],[120,140],[105,140],[125,160],[110,160],[130,180],[115,180],[160,200]])
polygon(wig2, BLACK, [[200,200],[200,155],[170,85],[85,60],[105,80],[90,80],[110,100],[95,100],[115,120],[100,120],[120,140],[105,140],[125,160],[110,160],[130,180],[115,180],[160,200]],1)
wig2 = pygame.transform.rotate(wig2, 20)
firstbigbird.blit(wig2,(40,310))


    
ellipse(firstbigbird, WHITE, (190,560,190,90)) #тело
ellipse(firstbigbird, WHITE, (350,575,90,35)) #шея

polygon(firstbigbird, YELLOW, [[470,565],[500,570],[505,580],[480,580]]) #клюв
polygon(firstbigbird, BLACK, [[470,565],[500,570],[505,580],[475,580]],1)

polygon(firstbigbird, YELLOW, [[460,590],[495,590],[505,580],[480,580]])
polygon(firstbigbird, BLACK, [[460,590],[495,590],[505,580],[480,580]],1)

ellipse(firstbigbird, WHITE, (420,555,60,45)) #голова
ellipse(firstbigbird, BLACK,(455,565,10,10)) #глаз


leg2 = pygame.Surface([400,400], pygame.SRCALPHA, 32)  #лапы
leg2 = leg2.convert_alpha()
arc(leg2,YELLOW,(90,0,40,40),1, 3, 3)
ellipse(leg2, WHITE, (0,0,90,30))

arc(leg2,YELLOW,(85,15,40,40),0.8, 3.8, 3)
arc(leg2,YELLOW,(90,5,40,40),1, 3, 3)
leg2 = pygame.transform.rotate(leg2, -20)

Leg2 = pygame.Surface([1000,1000], pygame.SRCALPHA, 32)
Leg2 = Leg2.convert_alpha()
ellipse(Leg2, WHITE, (0,0,35,90))
Leg2 = pygame.transform.rotate(Leg2, 20)
Leg2.blit(leg2,(-90,400))
firstbigbird.blit(Leg2,(230,280))
Leg2 = pygame.transform.rotate(Leg2, 9)
firstbigbird.blit(Leg2,(205,70))
screen.blit(firstbigbird,(-80,-20))
firstbigbird = pygame.transform.scale(firstbigbird, (183,259))
firstbigbird =pygame.transform.flip(firstbigbird, True, False)
screen.blit(firstbigbird,(400,290))
firstbigbird =pygame.transform.flip(firstbigbird, True, False)
firstbigbird = pygame.transform.scale(firstbigbird, (138,195))
screen.blit(firstbigbird,(250,300))
fish(50,650,16)
fish(400,670,17)
fish(450,590,12)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()

