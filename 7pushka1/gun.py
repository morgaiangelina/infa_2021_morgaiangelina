import math
from random import choice
from random import randint
import pygame
import sys
pygame.font.init()

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)

WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
k = 0.5
scores=0


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450, live=30):
        
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = live


    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        
        self.x += self.vx 
        self.y -= self.vy
        self.vy -= 1
        if (self.x-self.r)<0:
            self.x=self.r
            self.vx=-k*self.vx
        elif (self.x+self.r)>(WIDTH):
            self.vx=-k*self.vx
            self.x = WIDTH-self.r
        if (self.y-self.r)<0:
            self.y=self.r
            self.vy=-k*self.vy
        elif (self.y+self.r)>(HEIGHT):
            self.live-=10
            self.vy=-k*self.vy
            self.y = HEIGHT-self.r
    def draw(self):
        '''рисует объект'''
        pygame.draw.circle (self.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if math.sqrt((self.x-obj.x)**2+(self.y-obj.y)**2)<=(self.r+obj.r):
            return True
        else:
            return False
       


class Gun:
    def __init__(self, screen: pygame.Surface,x1=40,y1=450,x2=50,y2=450,width=10):
        """ Конструктор класса Gun

        Args:
        x1 - положение одного конца по горизонтали
        y1 - положение одного конца по вертикали
        x2 - положение другого конца горизонтали
        y2 - положение другого конца по вертикали
        width - ширина
        """
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        self.width=width

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
            self.x2=self.x1+self.f2_power * math.cos(self.an)
            self.y2=self.y1+self.f2_power * math.sin(self.an)
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        '''рисует объект'''
        pygame.draw.line(self.screen, self.color, (self.x1, self.y1), (self.x2, self.y2), self.width) 

    def power_up(self):
        '''увеличивает начальную скорость мяча и длину пушки, меняет цвет пушки в зависимости от'''
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY



class Target:
    def __init__ (self, screen: pygame.Surface):
        """ Конструктор класса ball

        Args:
        x - начальное положение цели по горизонтали
        y - начальное положение цели по вертикали
        """
        self.screen = screen
        self.points=True
        self.live = 1
        x = self.x = randint(600, 780)
        y = self.y = randint(300, 550)
        r = self.r = randint(2, 50)
        color = self.color = RED



    def hit(self, points=1):
        global scores
        """Попадание шарика в цель."""
        scores += points
        print('scores:',scores)


    def draw(self):
        '''рисует объект'''
        pygame.draw.circle (self.screen, self.color, (self.x, self.y), self.r)
        


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target(screen)
target2 = Target(screen)
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target1.draw()
    target2.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    i=0

    for b in balls:
        b.move()
        if b.hittest(target1) and target1.live:
            target1.live = 0
            target1.hit()
            target1 = Target(screen)
            balls.pop(i)
        else:
            if b.hittest(target2) and target2.live:
                target2.live = 0
                target2.hit()
                target2 = Target(screen)
                balls.pop(i)
        if b.live<=0:
            balls.pop(i)
        i+=1
            
    gun.power_up()

pygame.quit()
