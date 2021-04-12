from stuff.images import *
from classes.Player import player
import pygame


class Teleport(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image.fill(BLUE)
        self.image_orig = self.image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.hidden = False
        self.y_orig = y
        self.x_orig = x

    def update(self):
        pass

    def isOver(self):
        if self.rect.left <= player.rect.centerx <= self.rect.right and \
                self.rect.bottom >= player.rect.centery >= self.rect.top:
            return True

    def hide(self):
        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()
        self.hidden = True

    def unhide(self):
        self.image = self.image_orig
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x_orig
        self.rect.y = self.y_orig
        self.hidden = False


# Телепорты
teleport1 = Teleport(WIDTH / 2, 50 + WALL_SIZE)
teleport2 = Teleport(100 + WALL_SIZE, HEIGHT / 2)
teleport3 = Teleport(WIDTH - 100 - WALL_SIZE, HEIGHT / 2)
teleport_sprites = pygame.sprite.Group()
teleport_sprites.add(teleport1)
teleport_sprites.add(teleport2)
teleport_sprites.add(teleport3)