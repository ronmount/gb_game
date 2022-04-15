import pygame
import random
width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
img_dir = 'media/img/'
snd_dir = 'media/snd/'


class Auto_forward(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'forward'
        self.points = [(width // 2 + 50),        # Точки спауна по горизонтали
                       (width // 2 + 130),
                       (width // 2 + 210),
                       (width // 2 + 290)]
        self.image = pygame.image.load(img_dir + f"/auto/{random.randrange(5)}.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = random.choice(self.points)
        self.rect.y = 0