import pygame
import random
width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
img_dir = 'media/img/'
snd_dir = 'media/snd/'


class Tree(pygame.sprite.Sprite):
    def __init__(self):   #Функция, где указываем что будет у игрока
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + f"trees/{random.randint(1,16)}.png")

        self.rect = self.image.get_rect()

        self.rect.x = width//2
        self.rect.y = random.randrange(-height, 0, 50)

        self.side = random.choice(['left', 'right'])
        if self.side == 'left':
            self.rect.x = self.rect.x - 450 - random.randint(10, 350)
        elif self.side == 'right':
            self.rect.x = self.rect.x + 380 + random.randint(10, 350)
