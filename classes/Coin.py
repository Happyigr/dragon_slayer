from stuff.Methods import *
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
        self.rect.centerx = x
        self.rect.centery = y
        if self.rect.right >= WIDTH - WALL_SIZE:
            self.rect.right = WIDTH - WALL_SIZE
        if self.rect.left <= 0 + WALL_SIZE:
            self.rect.left = 0 + WALL_SIZE
        if self.rect.top <= 0 + WALL_SIZE:
            self.rect.top = 0 + WALL_SIZE
        if self.rect.bottom >= HEIGHT - WALL_SIZE:
            self.rect.bottom = HEIGHT - WALL_SIZE

    def update(self):
        pass

# Спрайты
coins_sprites = pygame.sprite.Group()
