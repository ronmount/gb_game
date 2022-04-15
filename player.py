import pygame

width = 1200
height = 600
img_dir = "media/img/"
snd_dir = "media/snd/"

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + "player.png")
        self.rect = self.image.get_rect()
        self.rect.x = width // 2
        self.rect.y = height - 150
