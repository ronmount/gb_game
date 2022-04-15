import pygame

width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
img_dir = 'media/img/'
snd_dir = 'media/snd/'


class Board(pygame.sprite.Sprite):
    def __init__(self, type):   # Здесь получаем тип бордюра
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(img_dir + "board.png")
        self.rect = self.image.get_rect()
        if type == 'right':      # В зависимости от типа располагаем и переворачиваем
             self.image = pygame.transform.flip(self.image, True, False)
             self.rect.centerx = width // 2 + 370
        else:
             self.rect.centerx = width // 2 - 370