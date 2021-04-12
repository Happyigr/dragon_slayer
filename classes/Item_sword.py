from stuff.images import *
from stuff.Methods import *
import pygame

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(screen_name)
clock = pygame.time.Clock()


class Item_sword(pygame.sprite.Sprite):
    def __init__(self, image, x, y, cost, damage, rate, num):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.num = num
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.chosen = False
        self.buyed = False
        self.cost = cost
        self.damage = damage
        self.rate = rate

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.rect.x < pos[0] < self.rect.x + self.rect.width:
            if self.rect.y < pos[1] < self.rect.y + self.rect.height:
                return True

        return False

    def update(self):
        if not self.buyed:
            draw_text(screen, str(self.cost), 30, self.rect.midbottom[0], self.rect.bottom)
        if self.buyed and not self.chosen:
            draw_text(screen, 'Купленно', 30, self.rect.midbottom[0], self.rect.bottom)
        if self.chosen and self.buyed:
            draw_text(screen, 'Выбрано', 30, self.rect.midbottom[0], self.rect.bottom)
        draw_text(screen, str(self.damage), 30, self.rect.midbottom[0], self.rect.bottom + 50)
        draw_text(screen, str(self.rate / 1000), 30, self.rect.midbottom[0], self.rect.bottom + 100)


# Товары
sword_1_item = Item_sword(armor_1_img, 300, 300, 0, 1, 1000, 1)
sword_2_item = Item_sword(armor_2_img, 450, 300, 100, 2, 700, 2)
sword_3_item = Item_sword(armor_3_img, 600, 300, 300, 3, 500, 3)
sword_4_item = Item_sword(armor_4_img, 750, 300, 500, 1, 200, 4)
item_array = [sword_1_item, sword_2_item, sword_3_item, sword_4_item]
item_sprites = pygame.sprite.Group()
item_sprites.add(sword_1_item)
item_sprites.add(sword_2_item)
item_sprites.add(sword_3_item)
item_sprites.add(sword_4_item)
