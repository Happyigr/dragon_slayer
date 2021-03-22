from game.stuff.Methods import *
from game.img.images import *
from game.classes.Player import player
import pygame


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(screen_name)
clock = pygame.time.Clock()


class Abilities(pygame.sprite.Sprite):
    def __init__(self, img, x, y, reload_time, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.image_orig = img
        self.ability_name = name
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.last_time_used = 0
        self.reload_time = reload_time
        self.reloaded = True

    def update(self):
        time = pygame.time.get_ticks()
        if not self.reloaded:
            reload = round(self.reload_time / 1000 - (time / 1000 - self.last_time_used / 1000), 1)
            self.image = pygame.Surface((0, 0))
            draw_text(screen, str(reload), 30, self.rect.centerx, self.rect.centery)
            if reload <= 0:
                self.reloaded = True
        else:
            self.image = self.image_orig


abilites_names = ['speedboost', 'superhit']
# Спрайты
superhit = Abilities(superhit_img_mini, 150, 75, player.SUPERHIT_RELOADTIME, 'superhit')
speedboost = Abilities(speedboost_img_mini, 75, 75, player.SPEEDBOOST_RELOADTIME, 'speedboost')

abilites_sprites = pygame.sprite.Group()
abilites_sprites.add(superhit)
abilites_sprites.add(speedboost)
