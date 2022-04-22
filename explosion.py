import pygame

snd_dir = 'media/snd/'
img_dir = 'media/img/'
width = 1200
height = 600


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.anim_speed = 2
        self.frame = 0
        self.anim = [pygame.transform.scale(
            pygame.image.load(img_dir + f'./explosion/{i}.png'),
            (100, 100)) for i in range(9)]
        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        self.image = self.anim[self.frame // self.anim_speed]  # Следующая картинка
        self.frame += 1
        if self.frame >= self.anim_speed * len(self.anim):  # Если последний кадр
            self.kill()
