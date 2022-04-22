import pygame
width = 1200  # ширина игрового окна
height = 600  # высота игрового окна
img_dir = 'media/img/'
snd_dir = 'media/snd/'


class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + 'arrow.png')
        self.image = pygame.transform.rotate(self.image, -200)  # Начальное положение
        self.rect = self.image.get_rect()
        self.copy = self.image  # Копия для вращения
        self.rect.center = (100, height - 100)  # Располагаем стрелку
        self.max_speed = 50
        self.min_speed = 0
        self.speed = 0

    def rotate(self, rotate):
        self.image = pygame.transform.rotate(self.copy, rotate)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP] and self.speed < self.max_speed:
            self.speed += 1
        elif keystate[pygame.K_DOWN] and self.speed > self.min_speed:
            self.speed -= 1
        self.rotate(-self.speed * 6)
