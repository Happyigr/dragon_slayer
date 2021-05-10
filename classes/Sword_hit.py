from stuff.images import *
from classes.Sword import sword_sprites
import pygame


class Sword_hit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        global sword
        for player_sword in sword_sprites:
            sword = player_sword
        self.image = pygame.Surface((200, 200))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = sword.rect.centerx
        self.rect.centery = sword.rect.centery

    def update(self):
        self.rect.centery = sword.rect.centery
        self.rect.centerx = sword.rect.centerx

# В sword_sprites всегда один меч (используемый)
# Спрайты
sword_hit_sprites = pygame.sprite.Group()
