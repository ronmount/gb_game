from player import Player
from speedometer import Speedometer
from arrow import Arrow
from bullet import Bullet

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
players = pygame.sprite.Group()
bullets = pygame.sprite.Group()

cars = pygame.sprite.Group()
boards = pygame.sprite.Group()

player = Player()
all_sprites.add(player)
players.add(player)

speedometer = Speedometer()
all_sprites.add(speedometer)

arrow = Arrow()
all_sprites.add(arrow)


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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.sound_shoot.play()
                bullet = Bullet(player)
                all_sprites.add(bullet)
                bullets.add(bullet)

    hit_boards = pygame.sprite.groupcollide(players, boards, False, False)
    hit_cars = pygame.sprite.groupcollide(players, cars, False, False)

    if hit_boards or hit_cars:
        player.speed = 0
        player.sound_explosion.play()
        player.kill()

    # Рендеринг (прорисовка)
    screen.fill(GREEN)  # Заливка заднего фона
    all_sprites.draw(screen)
    pygame.display.update()  # Переворачиваем экран
pygame.quit()  # Корректно завершаем игру