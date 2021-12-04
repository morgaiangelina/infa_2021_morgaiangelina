import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((550, 778))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 204, 0)
DARK_VIOLET = (25, 25, 112)
LIGHT_VIOLET = (123, 104, 238)
BLUE = (0, 0, 255)
PINK = (238, 130, 238)
DARK_PINK = (219, 112, 147)
ORANGE = (255, 127, 80)
LIGHT_GREEN = (32, 178, 170)


def draw_background(color1, color2, color3, color4, color5, color6):
    """
    Args:
        color1 - цвет первого сверху прямоугольника
        color2 - цвет второго сверху прямоугольника
        color3 - цвет третьего сверху прямоугольника
        color4 - цвет четвертого сверху прямоугольника
        color5 - цвет пятого сверху прямоугольника
        color6 - цвет шестого сверху прямоугольника
    """
    rect(screen, color1, (0, 0, 550, 71))
    rect(screen, color2, (0, 71, 550, 36))
    rect(screen, color3, (0, 107, 550, 70))
    rect(screen, color4, (0, 177, 550, 106))
    rect(screen, color5, (0, 283, 550, 106))
    rect(screen, color6, (0, 389, 550, 389))


def smallbird(x, y, size_increasement, angle):
    """
    Функция рисует птицу в виде галочки
    Args:
        x - горизонтальная координата левого верхнего угла поверхности рыбы
        y - вертикальная координата левого верхнего угла поверхности рыбы
        size_increasement - количество раз, в которое увеличить исходник рыбы
        angle - угол поворота
        """
    smallbird_surface = pygame.Surface([640, 480], pygame.SRCALPHA, 32)
    smallbird_surface = smallbird_surface.convert_alpha()
    arc(smallbird_surface, WHITE, (0, 0, 4 * size_increasement, 3 * size_increasement), 0, 2.7, 3)
    arc(smallbird_surface, WHITE, (4 * size_increasement, 0, 4 * size_increasement, 3 * size_increasement), 0.75, 3.14,
        3)
    smallbird_surface = pygame.transform.rotate(smallbird_surface, angle)
    screen.blit(smallbird_surface, (x, y))


def draw_bigbird(x, y, size_increasement, left):
    """
    Функция рисует белую птицу большую
    Args:
        x - координата слоя птицы по горизонтали
        y - по вертикали
        size_increasement - значение увеличения линейных размеров птицы
        left - приобретает значение True, когда птица смотрит клювом влево
        """
    firstbigbird = pygame.Surface([550, 778], pygame.SRCALPHA, 32)
    firstbigbird = firstbigbird.convert_alpha()
    polygon(firstbigbird, WHITE, [[200, 590], [150, 550], [140, 600], [190, 600]])  # хвост
    wig1 = pygame.Surface([400, 400], pygame.SRCALPHA, 32)  # крыло 1
    wig1 = wig1.convert_alpha()
    polygon(wig1, WHITE,
            [[200, 200], [200, 155], [170, 85], [85, 60], [105, 80], [90, 80], [110, 100], [95, 100], [115, 120],
             [100, 120], [120, 140], [105, 140], [125, 160], [110, 160], [130, 180], [115, 180], [160, 200]])
    polygon(wig1, BLACK,
            [[200, 200], [200, 155], [170, 85], [85, 60], [105, 80], [90, 80], [110, 100], [95, 100], [115, 120],
             [100, 120], [120, 140], [105, 140], [125, 160], [110, 160], [130, 180], [115, 180], [160, 200]], 1)
    wig1 = pygame.transform.rotate(wig1, 0)
    firstbigbird.blit(wig1, (140, 380))
    wig2 = pygame.Surface([400, 400], pygame.SRCALPHA, 32)
    wig2 = wig2.convert_alpha()
    polygon(wig2, WHITE,
            [[200, 200], [200, 155], [170, 85], [85, 60], [105, 80], [90, 80], [110, 100], [95, 100], [115, 120],
             [100, 120], [120, 140], [105, 140], [125, 160], [110, 160], [130, 180], [115, 180], [160, 200]])
    polygon(wig2, BLACK,
            [[200, 200], [200, 155], [170, 85], [85, 60], [105, 80], [90, 80], [110, 100], [95, 100], [115, 120],
             [100, 120], [120, 140], [105, 140], [125, 160], [110, 160], [130, 180], [115, 180], [160, 200]], 1)
    wig2 = pygame.transform.rotate(wig2, 20)
    firstbigbird.blit(wig2, (40, 310))
    ellipse(firstbigbird, WHITE, (190, 560, 190, 90))  # тело
    ellipse(firstbigbird, WHITE, (350, 575, 90, 35))  # шея
    polygon(firstbigbird, YELLOW, [[470, 565], [500, 570], [505, 580], [480, 580]])  # клюв
    polygon(firstbigbird, BLACK, [[470, 565], [500, 570], [505, 580], [475, 580]], 1)
    polygon(firstbigbird, YELLOW, [[460, 590], [495, 590], [505, 580], [480, 580]])
    polygon(firstbigbird, BLACK, [[460, 590], [495, 590], [505, 580], [480, 580]], 1)
    ellipse(firstbigbird, WHITE, (420, 555, 60, 45))  # голова
    ellipse(firstbigbird, BLACK, (455, 565, 10, 10))  # глаз
    leg2_surface1 = pygame.Surface([400, 400], pygame.SRCALPHA, 32)  # лапы
    arc(leg2_surface1, YELLOW, (90, 0, 40, 40), 1, 3, 3)
    ellipse(leg2_surface1, WHITE, (0, 0, 90, 30))
    arc(leg2_surface1, YELLOW, (85, 15, 40, 40), 0.8, 3.8, 3)
    arc(leg2_surface1, YELLOW, (90, 5, 40, 40), 1, 3, 3)
    leg2_surface1 = pygame.transform.rotate(leg2_surface1, -20)
    leg2_surface2 = pygame.Surface([1000, 1000], pygame.SRCALPHA, 32)
    leg2_surface2 = leg2_surface2.convert_alpha()
    ellipse(leg2_surface2, WHITE, (0, 0, 35, 90))
    leg2_surface2 = pygame.transform.rotate(leg2_surface2, 20)
    leg2_surface2.blit(leg2_surface1, (-90, 400))
    firstbigbird.blit(leg2_surface2, (230, 280))
    leg2_surface2 = pygame.transform.rotate(leg2_surface2, 9)
    firstbigbird.blit(leg2_surface2, (205, 70))
    firstbigbird = pygame.transform.scale(firstbigbird,
                                          (round(183 * size_increasement), round(259 * size_increasement)))
    if left:
        firstbigbird = pygame.transform.flip(firstbigbird, True, False)
    screen.blit(firstbigbird, (x, y))


clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    draw_background(DARK_VIOLET, LIGHT_VIOLET, PINK, DARK_PINK, ORANGE, LIGHT_GREEN)
    smallbird(320, 200, 20, -12)
    smallbird(340, 140, 10, -12)
    smallbird(320, 10, 15, 12)
    draw_bigbird(10, 80, 2.5, False)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

