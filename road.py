import pygame

width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
img_dir = 'media/img/'
snd_dir = 'media/snd/'


class Road(pygame.sprite.Sprite):
    def __init__(self):   #Функция, где указываем что будет у игрока
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + "road.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, 0)

