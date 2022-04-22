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
        self.max_speed = 25
        self.min_speed = 2
        self.speed = -random.randint(self.min_speed, self.max_speed)
        self.global_speed = 0
        self.global_min_speed = 0
        self.global_max_speed = 50
        self.rect.y = random.randrange(-height, 0, 300)
        self.sound = pygame.mixer.Sound(snd_dir + "explosion_car.mp3")

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP] and self.global_speed < self.global_max_speed:
            self.global_speed += 1
        if keystate[pygame.K_DOWN] and self.global_speed > self.global_min_speed:
            self.global_speed -=1
        self.rect.y += self.speed + self.global_speed
        if self.rect.top > height * 2:
            self.speed = -random.randint(self.min_speed, self.max_speed)
            self.rect.centerx = random.choice(self.points)
            self.rect.y = random.randrange(-height, 0, 300)