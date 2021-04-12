from stuff.Methods import *
# в Methods есть Settings
from stuff.images import wall_img
import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = wall_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Спрайты
wall_sprites = pygame.sprite.Group()
