import math
from random import choice
from random import randint
import pygame

FPS = 30
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = 0x7D7D7D
GAME_COLORS = [BLUE, YELLOW, GREEN, MAGENTA, CYAN]

width_of_window = 800
height_of_window = 600
v_max: int = 35


class Bullet:
    def __init__(self, gun, live=1, k=0.9):

        """ Конструктор класса Bullet
        Args:
        live - количество ударов мяча о пол до его исчезновения
        k - отношение модуля скорости снаряда после удара и до
        """
        self.k = k
        self.ball_screen = screen
        self.x = gun.x
        self.y = gun.y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = live
        self.damage = 1

    def draw(self):
        """Функция рисует снаряд"""
        pygame.draw.circle(self.ball_screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли снаряд с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения снаряда и цели. В противном случае возвращает False.
        """
        if math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) <= (self.r + obj.r):

            return True
        else:
            return False


class FirstTypeBullet(Bullet):
    def move(self):
        """Перемещение снаряда первого типа по прошествии единицы времени.
        Обычная гравитация.
        """

        self.x += self.vx
        self.y -= self.vy
        self.vy -= 1
        if (self.x - self.r) < 0:
            self.x = self.r
            self.vx = -self.k * self.vx
        elif (self.x + self.r) > width_of_window:
            self.vx = -self.k * self.vx
            self.x = width_of_window - self.r
        if (self.y - self.r) < 0:
            self.y = self.r
            self.vy = -self.k * self.vy
        elif (self.y + self.r) > height_of_window:
            self.live -= 1
            self.vy = -self.k * self.vy
            self.y = height_of_window - self.r


class SecondTypeBullet(Bullet):
    def move(self):
        """Перемещение мяча по прошествии единицы времени.
        Более сильная гравитация по сравнению с первым снарядом, есть сопротивление воздуха, даёт больше баллов
        """

        self.x += self.vx
        self.y -= self.vy
        self.vy -= (5+0.5*self.vy)
        self.vx -= (0.5 * self.vx)
        if (self.x - self.r) < 0:
            self.x = self.r
            self.vx = -self.k * self.vx
        elif (self.x + self.r) > width_of_window:
            self.vx = -self.k * self.vx
            self.x = width_of_window - self.r
        if (self.y - self.r) < 0:
            self.y = self.r
            self.vy = -self.k * self.vy
        elif (self.y + self.r) > height_of_window:
            self.live -= 3
            self.vy = -self.k * self.vy
            self.y = height_of_window - self.r


class Bomb(Bullet):
    def move(self):
        """
        Перемещение бомбы по прошествии единицы времени.
        Ослабленная гравитация
        """
        self.x += self.vx
        self.y -= self.vy
        self.vy -= 0.15
        if (self.x - self.r) < 0:
            self.live -= 3
        elif (self.x + self.r) > width_of_window:
            self.live -= 3
        if (self.y - self.r) < 0:
            self.live -= 3
        elif (self.y + self.r) > height_of_window:
            self.live -= 3

    def hittest_gun(self, obj):
        """Функция проверяет сталкивалкивается ли бомба с танком, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - obj.width <= self.x <= obj.x and obj.y - round(0.5 * obj.height) <= self.y <= obj.y +
            round(0.5 * obj.height)) or (obj.x - round(2.1*obj.width) <= self.x <= obj.x + round(1.1 * obj.width)
                                         and obj.y + round(0.5 * obj.height) <= self.y <= obj.y +
                                         round(1.3*obj.height)):
            obj.live -= self.damage
            return True
        else:
            return False

    def draw_bomb(self):
        """Функция рисует бомбу"""
        pygame.draw.circle(self.ball_screen, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(self.ball_screen, BLACK, (self.x, self.y), int(self.r / 2))


class Gun:
    def __init__(self, scores=0, live=1):
        """ Конструктор класса Gun
        Args:
        scores - количество очков в начале
        """
        self.scores = scores
        self.gun_screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.color2 = GREEN
        self.x = 140
        self.end_x = 115
        self.y = 450
        self.end_y = 415
        self.width_of_stick = 10
        self.width = 35
        self.height = 35
        self.vx = 5
        self.vy = 5
        self.live = live

    def fire2_start(self):
        """Запускание подготовки к выстрелу"""
        self.f2_on = 1

    def fire2_left_end(self, end_event, array_first_type_bullets):
        """Выстрел снарядом первого типа.
        Происходит при отпускании кнопки мыши.
        Args:
            end_event - событие отпускания мыши
            array_first_type_bullets - массив снарядов первого типа
        """
        new_ball = FirstTypeBullet(gun)
        self.an = math.atan2((end_event.pos[1] - new_ball.y), (end_event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        array_first_type_bullets.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def fire2_right_end(self, end_event, array_second_type_bullets):
        """Выстрел снарядом второго типа.
        Происходит при отпускании кнопки мыши.
        Args:
            end_event - событие отпускания мыши
            array_balls - массив снарядов второго типа
        """
        new_ball = SecondTypeBullet(gun)
        self.an = math.atan2((end_event.pos[1] - new_ball.y), (end_event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        array_second_type_bullets.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, targetting_event):
        """Прицеливание. Зависит от положения мыши.
        Args:
            targetting_event - событие изменение позиции мыши
        """
        if targetting_event:
            if (targetting_event.pos[0] - (self.x - 20)) != 0:
                self.an = math.atan((targetting_event.pos[1] - self.y) / (targetting_event.pos[0] - (self.x - 20)))
                self.end_x = self.x + self.f2_power * math.cos(self.an)
                self.end_y = self.y + self.f2_power * math.sin(self.an)
                if targetting_event.pos[0] - (self.x - 20) > 0:
                    self.end_x = self.end_x
                    self.end_y = self.end_y
                else:
                    self.end_x = 2 * self.x - self.end_x
                    self.end_y = 2 * self.y - self.end_y

        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def power_up(self):
        """увеличивает начальную скорость снаряда и длину пушки, меняет цвет пушки
        в зависимости от длительности нажатия"""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

    def hit_first_type_bullet(self, obj, points=1):
        """Попадание снаряда в цель.
        Args:
            points - шаг изменения количества очков при попадании в цель
            obj - объект столкновения
        Returns:
            self.scores - количество заработанных очков
        """
        if type(obj) == FirstTypeTarget:
            self.scores += points
        elif type(obj) == SecondTypeTarget:
            self.scores += 2 * points
        print('scores:', self.scores)
        return self.scores

    def hit_second_type_bullet(self, obj, points=3):
        """Попадание шарика в цель.
        Args:
            obj - объект столкновения
            points - шаг изменения количества очков при попадании в цель
        Returns:
            self.scores - количество заработанных очков
        """
        if type(obj) == FirstTypeTarget:
            self.scores += points
        elif type(obj) == SecondTypeTarget:
            self.scores += 2 * points
        print('scores:', self.scores)
        return self.scores


class GunEnemy(Gun):
    def draw(self):
        """Функция рисует неподвижного врага-танка танка игрока"""
        pygame.draw.rect(self.gun_screen, GREY, (self.x, self.y - round(0.5 * self.height), self.width, self.height))
        pygame.draw.rect(self.gun_screen, GREY, (
            self.x - round(0.7 * self.width), self.y + round(0.5 * self.height), round(2.4 * self.width),
            round(0.8 * self.height)))
        pygame.draw.circle(self.gun_screen, GREY, (self.x - round(0.7 * self.width), self.y + round(0.9 * self.height)),
                           round(0.4 * self.height))
        pygame.draw.circle(self.gun_screen, GREY, (self.x + round(1.7 * self.width), self.y + round(0.9 * self.height)),
                           round(0.4 * self.height))
        pygame.draw.circle(self.gun_screen, self.color2, (self.x - round(0.7 * self.width), self.y +
                                                          round(0.9 * self.height)),
                           round(0.35 * self.height))
        pygame.draw.circle(self.gun_screen, self.color2, (self.x + round(0.1 * self.width), self.y +
                                                          round(0.9 * self.height)),
                           round(0.35 * self.height))
        pygame.draw.circle(self.gun_screen, self.color2, (self.x + round(0.9 * self.width), self.y +
                                                          round(0.9 * self.height)),
                           round(0.35 * self.height))
        pygame.draw.circle(self.gun_screen, self.color2, (self.x + round(1.7 * self.width), self.y +
                                                          round(0.9 * self.height)),
                           round(0.35 * self.height))
        pygame.draw.line(self.gun_screen, self.color, (self.x, self.y), (self.end_x, self.end_y), self.width_of_stick)

    def fire2_end(self, end_event, array_bullets):
        """Выстрел бомбой из врага-танка.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        Args:
            end_event - событие отпускания мыши
            array_balls - массив снарядов
        """
        new_ball = Bomb(gun_enemy)
        self.an = math.atan2((end_event.pos[1] - new_ball.y), (end_event.pos[0] - new_ball.x))
        new_ball.vx = (self.f2_power * math.cos(self.an)) / 3
        new_ball.vy = - (self.f2_power * math.sin(self.an)) / 3
        array_bullets.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10


class Tank(Gun):
    def draw(self):
        """Функция рисует танк игрока"""
        pygame.draw.rect(self.gun_screen, self.color2, (self.x - self.width, self.y - round(0.5 * self.height),
                                                        self.width, self.height))
        pygame.draw.rect(self.gun_screen, self.color2, (
            self.x - round(1.7 * self.width), self.y + round(0.5 * self.height), round(2.4 * self.width),
            round(0.8 * self.height)))
        pygame.draw.circle(self.gun_screen, self.color2, (self.x - round(1.7 * self.width), self.y +
                                                          round(0.9 * self.height)),
                           round(0.4 * self.height))
        pygame.draw.circle(self.gun_screen, self.color2, (self.x + round(0.7 * self.width), self.y +
                                                          round(0.9 * self.height)),
                           round(0.4 * self.height))
        pygame.draw.circle(self.gun_screen, GREY, (self.x - round(1.7 * self.width), self.y + round(0.9 * self.height)),
                           round(0.35 * self.height))
        pygame.draw.circle(self.gun_screen, GREY, (self.x - round(0.9 * self.width), self.y + round(0.9 * self.height)),
                           round(0.35 * self.height))
        pygame.draw.circle(self.gun_screen, GREY, (self.x - round(0.1 * self.width), self.y + round(0.9 * self.height)),
                           round(0.35 * self.height))
        pygame.draw.circle(self.gun_screen, GREY, (self.x + round(0.7 * self.width), self.y + round(0.9 * self.height)),
                           round(0.35 * self.height))
        pygame.draw.line(self.gun_screen, self.color, (self.x, self.y), (self.end_x, self.end_y), self.width_of_stick)

    def move_d(self):
        """
        Сдвиг танка вправо, клавиша d
        """
        self.x += self.vx
        self.end_x += self.vx
        if (self.x + round(1.1 * self.width)) > width_of_window:
            self.x = width_of_window - round(1.1 * self.width)
            self.end_x -= self.vx

    def move_a(self):
        """
        Сдвиг танка влево, клавиша a
        """
        self.x -= self.vx
        self.end_x -= self.vx
        if (self.x - round(2.1 * self.width)) < 0:
            self.x = round(2.1 * self.width)
            self.end_x += self.vx

    def move_w(self):
        """
        Сдвиг танка вверх, клавиша w
        """
        self.y -= self.vy
        self.end_y -= self.vy
        if (self.y - round(0.5 * self.height)) < 0:
            self.y = round(0.5 * self.height)
            self.end_y += self.vy

    def move_s(self):
        """
        Сдвиг танка вниз, клавиша s
        """
        self.y += self.vy
        self.end_y += self.vy
        if (self.y + round(1.3 * self.height)) > height_of_window:
            self.y = height_of_window - round(1.3 * self.height)
            self.end_y -= self.vy


class Target:
    def __init__(self, live=1):
        """ Конструктор класса Target
        Args:
            live - приобретает значение 0 при попадании в цель, 1 - когда цель существует
        """

        self.target_screen = screen
        self.live = live
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(2, 50)
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        self.color = RED

    def draw(self):
        """Функция рисует цель"""
        pygame.draw.circle(self.target_screen, self.color, (self.x, self.y), self.r)


class FirstTypeTarget(Target):
    def move(self):
        """Перемещение первого типа цели по прошествии единицы времени"""
        self.x += self.vx
        self.y -= self.vy
        if (self.x - self.r) < 0:
            self.x = self.r
            self.vx = -self.vx
        elif (self.x + self.r) > width_of_window:
            self.vx = -self.vx
            self.x = width_of_window - self.r
        if (self.y - self.r) < 0:
            self.y = self.r
            self.vy = -self.vy
        elif (self.y + self.r) > height_of_window:
            self.vy = -self.vy
            self.y = height_of_window - self.r

    def create_bomb(self, array_bullets):
        """Сброс бомбы
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
            Args:
            array_bullets - массив снарядов
        """
        new_ball = Bomb(gun)
        new_ball.vx = self.vx / 2
        new_ball.vy = self.vy
        array_bullets.append(new_ball)


class SecondTypeTarget(Target):
    def move(self):
        """Перемещение второго типа цели по прошествии единицы времени, гравитация+ускорение при ударе о стену"""
        self.x += self.vx
        self.y -= self.vy
        self.vy -= 1
        if (self.x - self.r) < 0:
            self.x = self.r
            if abs(self.vx) <= v_max:
                self.vx = -2 * self.vx
            else:
                self.vx = -self.vx
        elif (self.x + self.r) > width_of_window:
            self.x = width_of_window - self.r
            if abs(self.vx) <= v_max:
                self.vx = -2 * self.vx
            else:
                self.vx = -self.vx
        if (self.y - self.r) < 0:
            self.y = self.r
            if abs(self.vy) <= v_max:
                self.vy = -2 * self.vy
            else:
                self.vy = -self.vy
        elif (self.y + self.r) > height_of_window:
            if abs(self.vy) <= v_max:
                self.vy = -2 * self.vy
            else:
                self.vy = -self.vy
            self.y = height_of_window - self.r


pygame.init()
screen = pygame.display.set_mode((width_of_window, height_of_window))

first_type_bullets = []
second_type_bullets = []
bombs = []

clock = pygame.time.Clock()
gun = Tank()
gun_enemy = GunEnemy()
gun_enemy.x = 700
gun_enemy.y = 400
target1 = FirstTypeTarget()
target2 = SecondTypeTarget()
finished = False
right_direction = left_direction = up_direction = down_direction = False
bomb_creating_time = 0

while not finished:
    screen.fill(WHITE)
    scores_font = pygame.font.Font(None, 50)
    scores_text = scores_font.render(str(gun.scores), True,
                                     (255, 0, 0))
    screen.blit(scores_text, (10, 10))
    gun.draw()
    gun_enemy.draw()
    target1.draw()
    target2.draw()

    for bullet in first_type_bullets:
        bullet.draw()
    for bullet in second_type_bullets:
        bullet.draw()
    for bomb in bombs:
        bomb.draw_bomb()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
            gun_enemy.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                gun.fire2_left_end(event, first_type_bullets)
                gun_enemy.fire2_end(event, bombs)
            elif event.button == 3:
                gun.fire2_right_end(event, second_type_bullets)
                gun_enemy.fire2_end(event, bombs)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
            gun_enemy.targetting(event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                right_direction = True
            elif event.key == pygame.K_a:
                left_direction = True
            elif event.key == pygame.K_w:
                up_direction = True
            elif event.key == pygame.K_s:
                down_direction = True
        elif event.type == pygame.KEYUP:
            right_direction = left_direction = up_direction = down_direction = False
        elif right_direction:
            gun.move_d()
        elif left_direction:
            gun.move_a()
        elif up_direction:
            gun.move_w()
        elif down_direction:
            gun.move_s()

    target1.move()
    target2.move()

    for first_type_bullet in first_type_bullets:
        first_type_bullet.move()
        if first_type_bullet.hittest(target1):
            target1.live = 0
            gun.hit_first_type_bullet(target1)
            target1 = FirstTypeTarget()
        else:
            if first_type_bullet.hittest(target2):
                target2.live = 0
                gun.hit_first_type_bullet(target2)
                target2 = SecondTypeTarget()
        if first_type_bullet.live <= 0:
            first_type_bullets.pop(first_type_bullets.index(first_type_bullet))

    for second_type_bullet in second_type_bullets:
        second_type_bullet.move()
        if second_type_bullet.hittest(target1):
            target1.live = 0
            gun.hit_second_type_bullet(target1)
            target1 = FirstTypeTarget()
            second_type_bullets.pop(second_type_bullets.index(i))
        else:
            if second_type_bullet.hittest(target2):
                target2.live = 0
                gun.hit_second_type_bullet(target2)
                target2 = SecondTypeTarget()
                second_type_bullets.pop(second_type_bullets.index(i))
        if second_type_bullet.live <= 0:
            second_type_bullets.pop(second_type_bullets.index(i))

    for bomb in bombs:
        bomb.move()
        bomb.hittest_gun(gun)
        if bomb.live <= 0:
            bombs.pop(bombs.index(bomb))
    if bomb_creating_time >= 120:
        target1.create_bomb(bombs)
        bombs[-1].x = target1.x
        bombs[-1].y = target1.y
        bomb_creating_time = 0
    bomb_creating_time += 1
    gun.power_up()
    gun_enemy.power_up()
    if gun.live <= 0:
        break

if not finished:
    screen.fill(BLACK)
    ending_font = pygame.font.Font(None, 100)
    game_is_over = ending_font.render('game is over', True,
                                      (255, 0, 0))
    screen.blit(game_is_over, (180, 250))
    pygame.display.update()

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

pygame.quit()
