import pygame
import pygame.draw as dr
from random import randint

pygame.init()

FPS = 30

a = 500
R = 50
R0 = 10  # минимальный радиус шариков
V = 100  # максимальная скорость шариков
screen = pygame.display.set_mode((a, a))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
N = 10
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
t = 0.1
balls = []
donuts = []


class Target:
    def __init__(self, balls_additional_points=1, donuts_additional_points=5):
        self.x = randint(R, a - R)  # массив координат шариков по горизонтали
        self.y = randint(R, a - R)  # массив координат шариков по вертикали
        self.vx = randint(-V, V)  # массив горизонтальных скоростей шариков
        self.vy = randint(-V, V)  # массив вертикальных скоростей шариков
        self.r = randint(R0, R)  # массив радиусов шариков
        self.color = COLORS[randint(0, 5)]  # массив цветов шариков
        self.ball_screen = screen
        self.balls_additional_points = balls_additional_points
        self.donuts_additional_points = donuts_additional_points


class Ball(Target):
    def move(self):
        self.x += self.vx * t
        self.y += self.vy * t
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
        """Функция рисует мяч"""
        dr.circle(screen, self.color, (self.x, self.y), self.r)

    def hittest(self, plus_scores, live):
        eventx, eventy = pygame.mouse.get_pos()
        if ((eventx - self.x) ** 2 + (eventy - self.y) ** 2) <= (self.r ** 2):
            plus_scores += self.balls_additional_points
            live += self.balls_additional_points
            print('A ball is catched! +', self.balls_additional_points, ' score! scores:', plus_scores)
            self.x = randint(R, a - R)
            self.y = randint(R, a - R)
            self.vx = randint(-V, V)
            self.vy = randint(-V, V)
            self.r = randint(R0, R)
            self.color = COLORS[randint(0, 5)]
        return plus_scores, live


class Donut(Target):
    def move(self):
        self.x += randint(-V, V) * 3 * t
        self.y += randint(-V, V) * 3 * t
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
        eventx, eventy = pygame.mouse.get_pos()
        if ((eventx - self.x) ** 2 + (eventy - self.y) ** 2) <= (self.r ** 2):
            if ((eventx - self.x) ** 2 + (eventy - self.y) ** 2) >= ((self.r ** 2) / 4):
                plus_scores += self.donuts_additional_points
                live += self.donuts_additional_points
                print('A ball is catched! +', self.donuts_additional_points, ' score! scores:', plus_scores)
                self.x = randint(R, a - R)
                self.y = randint(R, a - R)
                self.vx = randint(-V, V)
                self.vy = randint(-V, V)
                self.r = randint(R0, round(R/2))
                self.color = COLORS[randint(0, 5)]
        return plus_scores, live


class MainFunctions:
    def __init__(self, scores=0, max_number_of_one_type_objects=10, live_points=0):
        self.live_points = live_points
        self.scores = scores
        self.max_number_of_one_type_objects = max_number_of_one_type_objects

    def generate_array_of_objects(self, array_balls, array_donuts):
        number_of_balls = randint(2, self.max_number_of_one_type_objects)
        for i in range(number_of_balls):
            new_ball = Ball()
            array_balls.append(new_ball)
        number_of_donuts = randint(2, self.max_number_of_one_type_objects)
        for i in range(number_of_donuts):
            new_donut = Donut()
            array_donuts.append(new_donut)

    def draw_array_of_objects(self):
        screen.fill(BLACK)
        for i in balls:
            i.draw()
        for i in donuts:
            i.draw()

    def move_array_of_objects(self):
        for i in balls:
            i.move()
        for i in donuts:
            i.move()

    def click_check(self):
        for i in balls:
            self.scores, self.live_points = i.hittest(self.scores, self.live_points)
        for i in donuts:
            self.scores, self.live_points = i.hittest(self.scores, self.live_points)

    def save_scores(self):
        """создаёт файл с упорядоченным набором очков игроков"""
        results_file = open('scores.txt', 'a')
        results_file.write(name_of_player + '\n')
        results_file.write(str(game.scores) + '\n')
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


finished = False
pygame.display.update()
clock = pygame.time.Clock()
print('Введите имя игрока:')
name_of_player = input()

game = MainFunctions()

game.generate_array_of_objects(balls, donuts)
game.draw_array_of_objects()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.save_scores()
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.click_check()
    if game.live_points >= 10:
        game.generate_array_of_objects(balls, donuts)
        game.live_points = 0
    game.move_array_of_objects()
    game.draw_array_of_objects()
    pygame.display.update()

pygame.quit()
