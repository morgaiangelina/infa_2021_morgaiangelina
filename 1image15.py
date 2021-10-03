import pygame
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



def smallbird(name,x,y,n,angle):
    name = pygame.Surface([640,480], pygame.SRCALPHA, 32)
    name = name.convert_alpha()
    arc(name,WHITE,(0,0,4*n,3*n),0, 2.7, 3)
    arc(name,WHITE,(4*n,0,4*n,3*n),0.75, 3.14, 3)
    name = pygame.transform.rotate(name, angle)
    screen.blit(name,(x,y))
smallbird('1',50,200,20,-12)
smallbird('2',20,10,15,12)
smallbird('3',27,70,10,-19)


polygon(screen, WHITE, [[200,590],[150,550],[140,600],[190,600]])
wig1 = pygame.Surface([400,400], pygame.SRCALPHA, 32)
wig1 = wig1.convert_alpha()
polygon(wig1, WHITE, [[200,200],[200,155],[170,85],[85,60],[105,80],[90,80],[110,100],[95,100],[115,120],[100,120],[120,140],[105,140],[125,160],[110,160],[130,180],[115,180],[160,200]])
polygon(wig1, BLACK, [[200,200],[200,155],[170,85],[85,60],[105,80],[90,80],[110,100],[95,100],[115,120],[100,120],[120,140],[105,140],[125,160],[110,160],[130,180],[115,180],[160,200]],1)
wig1 = pygame.transform.rotate(wig1, 0)
screen.blit(wig1,(140,380))

polygon(screen, WHITE, [[200,590],[150,550],[140,600],[190,600]])
wig1 = pygame.Surface([400,400], pygame.SRCALPHA, 32)
wig1 = wig1.convert_alpha()
polygon(wig1, WHITE, [[200,200],[200,155],[170,85],[85,60],[105,80],[90,80],[110,100],[95,100],[115,120],[100,120],[120,140],[105,140],[125,160],[110,160],[130,180],[115,180],[160,200]])
polygon(wig1, BLACK, [[200,200],[200,155],[170,85],[85,60],[105,80],[90,80],[110,100],[95,100],[115,120],[100,120],[120,140],[105,140],[125,160],[110,160],[130,180],[115,180],[160,200]],1)
wig1 = pygame.transform.rotate(wig1, 0)
screen.blit(wig1,(140,380))

wig2 = pygame.Surface([400,400], pygame.SRCALPHA, 32)
wig2 = wig2.convert_alpha()
polygon(wig2, WHITE, [[200,200],[200,155],[170,85],[85,60],[105,80],[90,80],[110,100],[95,100],[115,120],[100,120],[120,140],[105,140],[125,160],[110,160],[130,180],[115,180],[160,200]])
polygon(wig2, BLACK, [[200,200],[200,155],[170,85],[85,60],[105,80],[90,80],[110,100],[95,100],[115,120],[100,120],[120,140],[105,140],[125,160],[110,160],[130,180],[115,180],[160,200]],1)
wig2 = pygame.transform.rotate(wig2, 20)
screen.blit(wig2,(40,310))


    
ellipse(screen, WHITE, (190,560,190,90))
ellipse(screen, WHITE, (350,575,90,35))

polygon(screen, YELLOW, [[470,565],[500,570],[505,580],[480,580]])
polygon(screen, BLACK, [[470,565],[500,570],[505,580],[475,580]],1)

polygon(screen, YELLOW, [[460,590],[495,590],[505,580],[480,580]])
polygon(screen, BLACK, [[460,590],[495,590],[505,580],[480,580]],1)

ellipse(screen, WHITE, (420,555,60,45))
ellipse(screen, BLACK,(455,565,10,10))


leg2 = pygame.Surface([400,400], pygame.SRCALPHA, 32)
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
screen.blit(Leg2,(230,280))
Leg2 = pygame.transform.rotate(Leg2, 9)
screen.blit(Leg2,(205,70))





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()
