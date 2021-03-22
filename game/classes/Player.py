from game.stuff.Methods import *
import pygame

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(screen_name)
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 50)
        self.speed = 5
        self.lives = 3
        #self.immune_time = 3000
        self.SPEEDBOOST_TIMEON = 0
        self.SPEEDBOOST_TIME = 3000
        self.SPEEDBOOST_RELOAD = True
        self.SPEEDBOOST_RELOADTIME = 5000
        self.SPEEDBOOST_ON = False
        self.SUPERHIT_TIMEON = 0
        self.SUPERHIT_DURATION = 200
        self.SUPERHIT_RELOAD = True
        self.SUPERHIT_RELOADTIME = 3000

    def update(self):
        time = pygame.time.get_ticks()
        # Проверка выхода за карту + Ходьба
        key_event = pygame.key.get_pressed()
        left = key_event[pygame.K_a]
        right = key_event[pygame.K_d]
        straight = key_event[pygame.K_w]
        back = key_event[pygame.K_s]
        if left and not self.rect.left - self.speed <= 0 + WALL_SIZE:
            self.rect.x -= self.speed
        if right and not self.rect.right + self.speed >= WIDTH - WALL_SIZE:
            self.rect.x += self.speed
        if straight and not self.rect.top - self.speed <= 0 + WALL_SIZE:
            self.rect.y -= self.speed
        if back and not self.rect.bottom + self.speed >= HEIGHT - WALL_SIZE:
            self.rect.y += self.speed
        # Способности
        # Проверка на перезарядку спидбуста
        if time - self.SPEEDBOOST_TIMEON >= self.SPEEDBOOST_RELOADTIME:
            self.SPEEDBOOST_RELOAD = True
        if time - self.SPEEDBOOST_TIMEON > self.SPEEDBOOST_TIME:
            self.speed = 5
            self.SPEEDBOOST_ON = False
        # Перезарядка суперудара
        if time - self.SUPERHIT_TIMEON >= self.SUPERHIT_RELOADTIME:
            self.SUPERHIT_RELOAD = True

    def speedboost(self):
        time = pygame.time.get_ticks()
        if self.SPEEDBOOST_RELOAD:
            self.speed = 15
            self.SPEEDBOOST_TIMEON = time
            self.SPEEDBOOST_RELOAD = False
            self.SPEEDBOOST_ON = True

    # Возвращает координаты в виде x y
    def get_coord(self):
        coord = [self.rect.x, self.rect.y]
        return coord


player = Player()
