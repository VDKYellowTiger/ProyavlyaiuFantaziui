import pygame
import random

from .constants import RED, WIDTH, HEIGHT


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(self.rect.width, WIDTH-self.rect.width), 0 + self.rect.height)

    def update(self):
        self.rect.y += random.randint(1, 6)

        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(self.rect.width, WIDTH - self.rect.width), 0 + self.rect.height)