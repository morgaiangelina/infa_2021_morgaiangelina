import pygame
import pygame.draw as dr
from random import randint

pygame.init()

FPS = 30
a = 500
r_max = 50
r_min = 10  # минимальный радиус шариков
v_max = 100  # максимальная скорость шариков
max_number_of_one_type_objects = 10
dt = 0.1
screen = pygame.display.set_mode((a, a))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

balls = []
donuts = []


class Target:
    """ Конструктор класса Target
    Args:
        balls_additional_points - количество добавленных очков при попадании в шарик
        donuts_additional_points - количество добавленных очков при попадании в пончик
    """

    def __init__(self, balls_additional_points=1, donuts_additional_points=5):
        self.x = randint(r_max, a - r_max)  # координата шарика или пончика по горизонтали
        self.y = randint(r_max, a - r_max)  # координата шарика или пончика по вертикали
        self.vx = randint(-v_max, v_max)  # горизонтальная скорость шарика или пончика
        self.vy = randint(-v_max, v_max)  # вертикальная скорость или пончикашарика
        self.r = randint(r_min, r_max)  # радиус шарика или внешний радиус пончика,
        # а также удвоенный внутренний радиус пончика
        self.color = COLORS[randint(0, 5)]  # цвет шарика или пончика
        self.ball_screen = screen
        self.balls_additional_points = balls_additional_points
        self.donuts_additional_points = donuts_additional_points


class Ball(Target):
    def move(self):
        """ Перемещение цели по прошествии единицы времени dt с учётом отбивания от стенок. Движение прямолинейное.
        """
        self.x += self.vx * dt
        self.y += self.vy * dt
        if (self.x - self.r) < 0:
            self.x = self.r
            self.vx = -self.vx
        elif (self.x + self.r) > a:
            self.vx = -self.vx
            self.x = a - self.r
        if (self.y - self.r) < 0:
            self.y = self.r
            self.vy = -self.vy
        elif (self.y + self.r) > a:
            self.vy = -self.vy
            self.y = a - self.r

    def draw(self):
        """Функция рисует шарик"""
        dr.circle(screen, self.color, (self.x, self.y), self.r)

    def hittest(self, plus_scores, live):
        """ Проверка попадания в площадь шарика.
        Args:
            plus_scores - количество очков
            live - положитльная переменная меньше, равная остатку деления очков на 10, при достижении 10 генерируется
            новая партия объектов
        Returns:
            plus_scores
            live
        """
        eventx, eventy = pygame.mouse.get_pos()
        if ((eventx - self.x) ** 2 + (eventy - self.y) ** 2) <= (self.r ** 2):
            plus_scores += self.balls_additional_points
            live += self.balls_additional_points
            print('A ball is caught! +', self.balls_additional_points, ' score! scores:', plus_scores)
            self.x = randint(r_max, a - r_max)
            self.y = randint(r_max, a - r_max)
            self.vx = randint(-v_max, v_max)
            self.vy = randint(-v_max, v_max)
            self.r = randint(r_min, r_max)
            self.color = COLORS[randint(0, 5)]
        return plus_scores, live


class Donut(Target):
    def move(self):
        """ Перемещение цели по прошествии единицы времени dt с учётом отбивания от стенок. Движение броуновское.
        """
        self.x += randint(-v_max, v_max) * 3 * dt
        self.y += randint(-v_max, v_max) * 3 * dt
        if (self.x - self.r) < 0:
            self.x = self.r
        elif (self.x + self.r) > a:
            self.x = a - self.r
        if (self.y - self.r) < 0:
            self.y = self.r
        elif (self.y + self.r) > a:
            self.vy = -self.vy
            self.y = a - self.r

    def draw(self):
        """Функция рисует мяч"""
        dr.circle(screen, self.color, (self.x, self.y), self.r, round(self.r / 2))

    def hittest(self, plus_scores, live):
        """ Проверка попадания в площадь пончика.
        Args:
            plus_scores - количество очков
            live - положитльная переменная меньше, равная остатку деления очков на 10, при достижении 10 генерируется
            новая партия объектов
        Returns:
            plus_scores
            live - о
        """
        eventx, eventy = pygame.mouse.get_pos()
        if ((eventx - self.x) ** 2 + (eventy - self.y) ** 2) <= (self.r ** 2):
            if ((eventx - self.x) ** 2 + (eventy - self.y) ** 2) >= ((self.r ** 2) / 4):
                plus_scores += self.donuts_additional_points
                live += self.donuts_additional_points
                print('A ball is caught! +', self.donuts_additional_points, ' score! scores:', plus_scores)
                self.x = randint(r_max, a - r_max)
                self.y = randint(r_max, a - r_max)
                self.vx = randint(-v_max, v_max)
                self.vy = randint(-v_max, v_max)
                self.r = randint(r_min, round(r_max/2))
                self.color = COLORS[randint(0, 5)]
        return plus_scores, live


class Scores:
    def __init__(self, scores=0, live_points=0):
        """"Конструктор класса Scores
        Args:
            scores - количество очков
            live_points - положитльная переменная меньше, равная остатку деления очков на 10, при достижении 10
            генерируется
            новая партия объектов
        """
        self.live_points = live_points
        self.scores = scores

    def click_check(self):
        """"Проверка попадания в цели и обновление счёта очков
        """
        for i in balls:
            self.scores, self.live_points = i.hittest(self.scores, self.live_points)
        for i in donuts:
            self.scores, self.live_points = i.hittest(self.scores, self.live_points)

    def save_scores(self):
        """создаёт файл с упорядоченным набором очков игроков"""
        results_file = open('scores.txt', 'a')
        results_file.write(name_of_player + '\n')
        results_file.write(str(self.scores) + '\n')
        results_file.close()
        counting_variable = 0
        scores_statistics = []
        names_data = []
        results_file = open('scores.txt', 'r')
        while True:
            line = results_file.readline()
            if not line:
                break
            if (-1) ** counting_variable == 1:
                name = str(line)
                name.replace('\n', '')
                names_data.append(name)
            elif (-1) ** counting_variable == -1:
                number_of_scores = str(line)
                number_of_scores.replace('\n', '')
                number_of_scores = int(number_of_scores)
                scores_statistics.append(number_of_scores)
            counting_variable += 1
        results_file.close()
        results_file = open('scores.txt', 'w')
        while max(scores_statistics) > -1:
            results_file.write(names_data[scores_statistics.index(max(scores_statistics))])
            results_file.write(str(scores_statistics[scores_statistics.index(max(scores_statistics))]) + '\n')
            scores_statistics[scores_statistics.index(max(scores_statistics))] = -1
        results_file.close()


def generate_array_of_objects(array_balls, array_donuts):
    """Создание массива пончиков и массива шариков или регенерация рандомных значений
    Args:
        array_balls - массив шариков
        array_donuts - массив пончиков
    """
    number_of_balls = randint(2, max_number_of_one_type_objects)
    for i in range(number_of_balls):
        new_ball = Ball()
        array_balls.append(new_ball)
    number_of_donuts = randint(2, max_number_of_one_type_objects)
    for i in range(number_of_donuts):
        new_donut = Donut()
        array_donuts.append(new_donut)


def draw_array_of_objects():
    """Рисует массив пончиков и массив шариков
    """
    screen.fill(BLACK)
    for i in balls:
        i.draw()
    for i in donuts:
        i.draw()


def move_array_of_objects():
    """Изменение координат целей с прошествием единицы времени
    """
    for i in balls:
        i.move()
    for i in donuts:
        i.move()


finished = False
pygame.display.update()
clock = pygame.time.Clock()
print('Введите имя игрока:')
name_of_player = input()
game = Scores()
generate_array_of_objects(balls, donuts)
draw_array_of_objects()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.save_scores()
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.click_check()
    if game.live_points >= 10:
        balls.clear()
        donuts.clear()
        generate_array_of_objects(balls, donuts)
        game.live_points = 0
    move_array_of_objects()
    draw_array_of_objects()
    pygame.display.update()

pygame.quit()
