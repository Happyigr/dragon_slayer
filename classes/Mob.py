from stuff.Methods import *
from stuff.images import *
from classes.Player import player
import random
import pygame


# не делать размер больше WALL_SIZE, будут проблемы с столкновениями
class Mob(pygame.sprite.Sprite):
    def __init__(self, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        rand_num = random.random()
        if rand_num >= 0.9:
            self.type = 'big'
            self.image = pygame.Surface((90, 90))
            self.image.fill(RED)
            self.lives = random.randrange(10, 15)
            self.money = (15, 30)
        elif rand_num >= 0.8:
            self.type = 'medium'
            self.image = pygame.Surface((50, 50))
            self.image.fill(RED)
            self.lives = random.randrange(5, 10)
            self.money = (5, 10)
        else:
            self.type = 'small'
            self.image = pygame.Surface((25, 25))
            self.image.fill(RED)
            self.lives = random.randrange(1, 5)
            self.money = (1, 5)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        # Время спавна
        self.spawn_time = pygame.time.get_ticks()
        # Время последнего изменения скорости
        self.changed_speed_time = pygame.time.get_ticks()
        self.speed = (0, 0)
        self.min_speed = -4
        self.max_speed = 4
        # Время после которого моб будет менять скорость
        self.speed_change_rate = random.randrange(2000, 4000)
        # Время которое моб будет бездействовать в начале нового уровня
        self.afk_time = 200

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        time = pygame.time.get_ticks()
        # Ходьба мобов
        draw_text(screen, str(self.lives), 30, self.rect.centerx, self.rect.top - 30)
        # Если первый раз меняется скорость, поменять скорость после afk_time
        if time - self.spawn_time > self.afk_time and self.changed_speed_time == self.spawn_time:
            self.walking_choise(time)
        # Выбор варианта ходьбы моба после определенного времени
        if time - self.changed_speed_time >= self.speed_change_rate:
            self.walking_choise(time)

    # Выбор тактики ходьбы
    def walking_choise(self, time):
        rand_num = random.random()
        if rand_num >= 0.9:
            self.speed = (0, 0)
        elif rand_num >= 0.7:
            self.speed = (self.to_player_go()[0], self.to_player_go()[1])
        else:
            self.speed = (random.randrange(self.min_speed, self.max_speed),
                          random.randrange(self.min_speed, self.max_speed))
        self.changed_speed_time = time

    # Скорость для движения к игроку в виде x y
    def to_player_go(self):
        speeds = []
        time = 30
        sx = player.rect.centerx - self.rect.centerx
        sy = player.rect.centery - self.rect.centery
        speedx = sx / time
        speedy = sy / time
        # Делим чтобы моб двигался не быстрее чем 5 пикселей в милисекунду
        while not (self.min_speed <= speedx <= self.max_speed) and \
                not (self.min_speed <= speedy <= self.max_speed) \
                and speedy == 0 and speedx == 0:
            time += 5
            speedx = sx / time
            speedy = sy / time
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
