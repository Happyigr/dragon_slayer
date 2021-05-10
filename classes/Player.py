from classes.Wall import wall_sprites
from stuff.images import player_img
from stuff.Map import *
import pygame


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(screen_name)
clock = pygame.time.Clock()


class Player_copy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 50)
        self.speed = (0, 0)     # Скорость по х и у
        self.speed_value = 5    # Скорость игрока в одну сторону
        self.lives = 3
        self.SPEEDBOOST_TIMEON = 0
        self.SPEEDBOOST_TIME = 3000
        self.SPEEDBOOST_RELOAD = True
        self.SPEEDBOOST_RELOADTIME = 5000
        self.SPEEDBOOST_ON = False
        self.SUPERHIT_TIMEON = 0
        self.SUPERHIT_DURATION = 200
        self.SUPERHIT_RELOAD = True
        self.SUPERHIT_RELOADTIME = 2000


    def update(self):
        time = pygame.time.get_ticks()
        # Проверка выхода за карту + Ходьба
        key_event = pygame.key.get_pressed()
        left = key_event[pygame.K_a]
        right = key_event[pygame.K_d]
        straight = key_event[pygame.K_w]
        back = key_event[pygame.K_s]
        self.speed = (0, 0)
        if left:
            self.speed = (-self.speed_value, 0)
        if right:
            self.speed = (self.speed_value, 0)
        if straight:
            self.speed = (0, -self.speed_value)
        if back:
            self.speed = (0, self.speed_value)
        if left and straight:
            self.speed = (-self.speed_value, -self.speed_value)
        if left and back:
            self.speed = (-self.speed_value, self.speed_value)
        if right and straight:
            self.speed = (self.speed_value, -self.speed_value)
        if right and back:
            self.speed = (self.speed_value, self.speed_value)
        self.collision_check()
        # Способности
        # Проверка на перезарядку спидбуста
        if time - self.SPEEDBOOST_TIMEON >= self.SPEEDBOOST_RELOADTIME:
            self.SPEEDBOOST_RELOAD = True
        if time - self.SPEEDBOOST_TIMEON > self.SPEEDBOOST_TIME:
            self.speed_value = 5
            self.SPEEDBOOST_ON = False
        # Перезарядка суперудара
        if time - self.SUPERHIT_TIMEON >= self.SUPERHIT_RELOADTIME:
            self.SUPERHIT_RELOAD = True

    def collision_check(self):
        # Проверка не удариться ли игрок со стеной
        # по х
        player_copy.rect.center = self.rect.center
        player_copy.rect.x += self.speed[0]
        if pygame.sprite.spritecollide(player_copy, wall_sprites, False):
            self.speed = (0, self.speed[1])
        # по у
        player_copy.rect.center = self.rect.center
        player_copy.rect.y += self.speed[1]
        if pygame.sprite.spritecollide(player_copy, wall_sprites, False):
            self.speed = (self.speed[0], 0)
        # прибавка скорости
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def speedboost(self):
        time = pygame.time.get_ticks()
        if self.SPEEDBOOST_RELOAD:
            self.speed_value = 15
            self.SPEEDBOOST_TIMEON = time
            self.SPEEDBOOST_RELOAD = False
            self.SPEEDBOOST_ON = True

# Спрайты
player = Player()
player_copy = Player_copy()
