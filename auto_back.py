import pygame
import random
width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
img_dir = 'media/img/'
snd_dir = 'media/snd/'


class Auto_back(pygame.sprite.Sprite):
    def __init__(self):   # Функция, где указываем что будет у игрока
        pygame.sprite.Sprite.__init__(self)
        self.type = 'back'
        self.points = [(width // 2 - 50),
                       (width // 2 - 130),
                       (width // 2 - 210),
                       (width // 2 - 290)]
        self.image = pygame.image.load(img_dir + f"auto/{random.randrange(5)}.png")
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice(self.points), 0)
