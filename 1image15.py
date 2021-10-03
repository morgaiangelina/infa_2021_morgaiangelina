import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((550, 778))
WHITE =(255,255,255)
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



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()
