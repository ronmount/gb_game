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
