from road import Road
from board import Board
from tree import Tree

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
GOLD = "#FFD700"

snd_dir = "media/snd/"
img_dir = "media/img/"

all_sprites = pygame.sprite.Group()

road = Road()
all_sprites.add(road)

board_left = Board('left')
board_right = Board('right')
all_sprites.add([board_left, board_right])

tree = Tree()
all_sprites.add(tree)

# Создаем игровой экран
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)  # Заголовок окна
icon = pygame.image.load(img_dir + 'icon.png')  # загружаем файл с иконкой
pygame.display.set_icon(icon)  # устанавливаем иконку в окно

timer = pygame.time.Clock()  # Создаем таймер pygame
run = True

pygame.mixer.music.load(snd_dir + 'music.mp3')
pygame.mixer.music.set_volume(0.03)
pygame.mixer.music.play(-1)


def draw_text(screen, text, size, x, y, color): # Функция для отображения текста на экране
    font_name = './font.ttf'
    font = pygame.font.Font(font_name, size)     # Шрифт выбранного типа и размера
    text_image = font.render(text, True, color)  # Превращаем текст в картинку
    text_rect = text_image.get_rect()            # Задаем рамку картинки с текстом
    text_rect.center = (x,y)           # Переносим центр текста в указанные координаты
    screen.blit(text_image, text_rect)


while run:  # Начинаем бесконечный цикл
    timer.tick(fps)  # Контроль времени (обновление игры)
    all_sprites.update()
    for event in pygame.event.get():  # Обработка ввода (события)
        if event.type == pygame.QUIT:  # Проверить закрытие окна
            run = False  # Завершаем игровой цикл
    # Рендеринг (прорисовка)
    screen.fill(GREEN)  # Заливка заднего фона
    all_sprites.draw(screen)
    draw_text(screen, r'Score = {player.score}', 50, 120, 20, GOLD)
    pygame.display.update()  # Переворачиваем экран
pygame.quit()  # Корректно завершаем игру