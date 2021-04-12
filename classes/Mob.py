from stuff.Methods import *
from stuff.images import *
from classes.Wall import wall_sprites
from classes.Player import player
import random
import pygame


class Mob_copy(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        if name == 'big':
            self.image = pygame.Surface((100, 100))
        if name == 'medium':
            self.image = pygame.Surface((50, 50))
        if name == 'small':
            self.image = pygame.Surface((25, 25))
        self.rect = self.image.get_rect()


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if random.random() >= 0.9:
            self.name = 'big'
            self.image = pygame.Surface((100, 100))
            self.image.fill(RED)
            self.lives = random.randrange(10, 15)
        elif random.random() >= 0.8:
            self.name = 'medium'
            self.image = pygame.Surface((50, 50))
            self.image.fill(RED)
            self.lives = random.randrange(5, 10)
        else:
            self.name = 'small'
            self.image = pygame.Surface((25, 25))
            self.image.fill(RED)
            self.lives = random.randrange(1, 5)
        self.rect = self.image.get_rect()
        # подбираем подходящие координаты
        self.rect.x = random.randrange(WALL_SIZE + self.rect.width, WIDTH - WALL_SIZE - self.rect.width)
        self.rect.y = random.randrange(WALL_SIZE + self.rect.height, HEIGHT - WALL_SIZE - self.rect.height)
        while pygame.sprite.spritecollide(self, wall_sprites, False):
            self.rect.x = random.randrange(WALL_SIZE + self.rect.width, WIDTH - WALL_SIZE - self.rect.width)
            self.rect.y = random.randrange(WALL_SIZE + self.rect.height, HEIGHT - WALL_SIZE - self.rect.height)
        # Время спавна
        self.spawn_time = pygame.time.get_ticks()
        # Время последнего изменения скорости
        self.changed_speed_time = pygame.time.get_ticks()
        self.speed = (0, 0)
        # Время после которого моб будет менять скорость
        self.speed_change_rate = random.randrange(2000, 4000)
        # Время которое моб будет бездействовать в начале нового уровня
        self.afk_time = 200

    # Скорость для движения к игроку в виде x y
    def update(self):
        time = pygame.time.get_ticks()
        # Ходьба мобов
        draw_text(screen, str(self.lives), 30, self.rect.centerx, self.rect.top - 30)
        # Прибавляем к времени изменения скорости 4с чтобы после спавна моб сразу поменял скорость
        if time - self.spawn_time > self.afk_time and self.changed_speed_time == self.spawn_time:
            self.changed_speed_time -= 4000
        # Выбор варианта ходьбы моба после определенного времени
        if time - self.changed_speed_time >= self.speed_change_rate:
            self.walking_choise(time)
        # ходьба
        self.collision_check_and_walking()

    # Ходьба
    def collision_check_and_walking(self):
        # Проверка не удариться ли моб со стеной
        hits = pygame.sprite.spritecollide(self, wall_sprites, False)
        for hit in hits:
            speed_x = self.speed[0]
            speed_y = self.speed[1]
            self.speed = (speed_x * -1, speed_y * -1)
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    # Выбор тактики ходьбы
    def walking_choise(self, time):
        rand_num = random.random()
        if rand_num >= 0.9:
            self.speed = (0, 0)
        elif rand_num >= 0.7:
            self.speed = (self.to_player_go()[0], self.to_player_go()[1])
        else:
            self.speed = (random.randrange(-5, 5), random.randrange(-5, 5))
        self.changed_speed_time = time

    def to_player_go(self):
        speeds = []
        time = 30
        sx = player.rect.centerx - self.rect.centerx
        sy = player.rect.centery - self.rect.centery
        speedx = sx / time
        speedy = sy / time
        # Делим чтобы моб двигался не быстрее чем 5 пикселей в милисекунду
        while not (-5 <= speedx <= 5) and not (-5 <= speedy <= 5) and speedy == 0 and speedx == 0:
            time += 5
            speedy = sy / time
            speedx = sx / time
        # Ещё уменьшение скорости, чтобы игрок мог среагировать
        if random.random() >= 0.8:
            speedx /= 2
            speedy /= 2
        else:
            speedx /= 3
            speedy /= 3
        speeds.append(speedx)
        speeds.append(speedy)
        return speeds



# Спрайты
mobs = pygame.sprite.Group()
