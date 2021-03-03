import pygame
from os import path
import random
from Variables import *
from Methods import *


def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


def sword_spawn():
    sword = Sword(player.rect.x, player.rect.y)
    all_sprites.add(sword)
    sword_sprite.add(sword)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        key_event = pygame.key.get_pressed()
        left = key_event[pygame.K_a]
        right = key_event[pygame.K_d]
        straight = key_event[pygame.K_w]
        back = key_event[pygame.K_s]
        if left:
            self.rect.x -= 5
        if right:
            self.rect.x += 5
        if straight:
            self.rect.y -= 5
        if back:
            self.rect.y += 5
        # Проверка выхода за карту
        if self.rect.right >= WIDTH - 50:
            self.rect.right = WIDTH - 50
        if self.rect.left <= 0 + 50:
            self.rect.left = 0 + 50
        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
        if self.rect.top <= 0 + 50:
            self.rect.top = 0 + 50

    def hit(self):
        sword_spawn()


class Sword(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.damage = None
        self.range = None

    def update(self):
        pass


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(mobs_values_x)
        self.rect.y = random.choice(mobs_values_y)
        self.speedx = random.randrange(-5, 5)
        self.speedy = random.randrange(-5, 5)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Проверка выхода за карту
        if self.rect.right >= WIDTH - 50:
            self.rect.right = WIDTH - 50
            self.speedx = random.randrange(-5, 5)
        if self.rect.left <= 0 + 50:
            self.rect.left = 0 + 50
            self.speedx = random.randrange(-5, 5)
        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.speedy = random.randrange(-5, 5)
        if self.rect.top <= 0 + 50:
            self.rect.top = 0 + 50
            self.speedy = random.randrange(-5, 5)


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(screen_name)
clock = pygame.time.Clock()

# Спрайты
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
sword_sprite = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Цикл игры
for i in range(8):
    newmob()
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        # Удар
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.hit()

    # Проверка не убил ли меч моба
    hits = pygame.sprite.groupcollide(mobs, sword_sprite, True, False, pygame.sprite.collide_circle)
    for hit in hits:
        newmob()

    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()