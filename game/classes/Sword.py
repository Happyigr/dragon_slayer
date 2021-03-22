from game.classes.Item_sword import sword_1_item
from game.classes.Player import player
from game.img.images import *
import pygame


class Sword(pygame.sprite.Sprite):
    def __init__(self, damage, rate):
        pygame.sprite.Sprite.__init__(self)
        self.image = sword_img_mini
        self.image_orig = self.image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.midbottom = player.rect.center
        self.x = self.rect.x
        self.y = self.rect.y
        self.speedx = 0
        self.speedy = 0
        self.damage = damage
        self.rate = rate
        self.range = None
        self.angle = 0
        self.last_hit = 0

    def update(self):
        mouse_coord = pygame.mouse.get_pos()
        mouse_x = mouse_coord[0]
        mouse_y = mouse_coord[1]
        self.rect.centerx = mouse_x
        self.rect.centery = mouse_y
        # ходьба меча
        self.rotate()
        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy
        if self.rect.centerx > player.rect.centerx + 50:
            self.rect.centerx = player.rect.centerx + 50
        if self.rect.centerx < player.rect.centerx - 50:
            self.rect.centerx = player.rect.centerx - 50
        if self.rect.centery > player.rect.centery + 50:
            self.rect.centery = player.rect.centery + 50
        if self.rect.centery < player.rect.centery - 50:
            self.rect.centery = player.rect.centery - 50

    def rotate(self):
        # Поворот картинки
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - player.rect.x, mouse_y - player.rect.y
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x) - 90
        if self.angle >= 360:
            self.angle = 0
        self.image = pygame.transform.rotate(self.image_orig, int(self.angle))
        # Поворот по х и у
        time = 30
        sx = player.rect.centerx - mouse_x
        sy = player.rect.centery - mouse_y
        self.speedx = sx / time
        self.speedy = sy / time


# Спрайты
sword = Sword(sword_1_item.damage, sword_1_item.rate)
sword_sprites = pygame.sprite.Group()
sword_sprites.add(sword)
