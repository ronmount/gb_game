from auto_forward import Auto_forward
from auto_back import Auto_back


import pygame

pygame.init()  # Инициализируем модуль pygame

width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
fps = 30  # частота кадров в секунду
game_name = "Racing"  # название нашей игры

# Цвета
BLACK = "#000000"
WHITE = "#FFFFFF"
RED = "#FF0000"
GREEN = "#008000"
BLUE = "#0000FF"
CYAN = "#00FFFF"

snd_dir = "media/snd/"
img_dir = "media/img/"

all_sprites = pygame.sprite.Group()

auto_forward = Auto_forward()
all_sprites.add(auto_forward)

auto_back = Auto_back()
all_sprites.add(auto_back)

# Создаем игровой экран
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)  # Заголовок окна
icon = pygame.image.load(img_dir + 'icon.png')  # загружаем файл с иконкой
pygame.display.set_icon(icon)  # устанавливаем иконку в окно

timer = pygame.time.Clock()  # Создаем таймер pygame
run = True

while run:  # Начинаем бесконечный цикл
    timer.tick(fps)  # Контроль времени (обновление игры)
    all_sprites.update()
    for event in pygame.event.get():  # Обработка ввода (события)
        if event.type == pygame.QUIT:  # Проверить закрытие окна
            run = False  # Завершаем игровой цикл
    # Рендеринг (прорисовка)
    screen.fill(GREEN)  # Заливка заднего фона
    all_sprites.draw(screen)
    pygame.display.update()  # Переворачиваем экран
pygame.quit()  # Корректно завершаем игру