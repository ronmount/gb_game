import pygame
width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
img_dir = 'media/img/'
snd_dir = 'media/snd/'


class Speedometer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + 'speedometr.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = (100, height - 100)  # Левый нижний угол