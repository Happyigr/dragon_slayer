from game.img.images import *
from game.classes.Sword import sword
import pygame


class Sword_hit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1000, 1000))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = sword.rect.centerx
        self.rect.centery = sword.rect.centery

    def update(self):
        self.rect.centerx = sword.rect.centerx
        self.rect.centery = sword.rect.centery


# Спрайты
sword_hit_sprites = pygame.sprite.Group()
