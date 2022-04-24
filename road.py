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
        self.max_speed = 50
        self.min_speed = 0
        self.speed = 0

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP] and self.speed < self.max_speed:
            self.speed += 1
        elif keystate[pygame.K_DOWN] and self.speed > self.min_speed:
            self.speed -= 1
        self.rect.y += self.speed

        if self.rect.top >= 0:
            self.rect.bottom = height

