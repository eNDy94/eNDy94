import pygame
import random


class Enemies(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1050, 1150)
        self.rect.y = 768 - 267 - (random.randrange(20, 300) + 60)
        self.speedx = random.randrange(3, 8)

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < -100:
            self.rect.x = random.randrange(1050, 1150)
            self.rect.y = 768 - 267 - (random.randrange(20, 300) + 60)