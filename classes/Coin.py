from stuff.Methods import *
from classes.Wall import wall_sprites
import random
import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        if random.random() >= 0.8:
            self.image = pygame.Surface((20, 20))
            self.image.fill(YELLOW)
            self.cost = 10
        elif random.random() >= 0.5:
            self.image = pygame.Surface((15, 15))
            self.image.fill(GREY)
            self.cost = 5
        else:
            self.image = pygame.Surface((10, 10))
            self.image.fill(BROWN)
            self.cost = 1
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(-50, 50) + x
        self.rect.centery = random.randrange(-50, 50) + y
        while pygame.sprite.spritecollide(self, wall_sprites, False):
            self.rect.centerx = random.randrange(-50, 50) + x
            self.rect.centery = random.randrange(-50, 50) + y

    def update(self):
        pass

# Спрайты
coins_sprites = pygame.sprite.Group()
