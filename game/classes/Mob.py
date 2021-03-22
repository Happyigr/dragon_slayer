from game.stuff.Methods import *
from game.img.images import *
from game.classes.Player import player
import random
import pygame


# Скорость для движения к игроку в виде x y
def to_player_go(mob):
    speeds = []
    time = 30
    sx = player.rect.centerx - mob.rect.centerx
    sy = player.rect.centery - mob.rect.centery
    speedx = sx / time
    speedy = sy / time
    while not (-5 <= speedx <= 5) and not (-5 <= speedy <= 5) and speedy == 0 and speedx == 0:
        time += 5
        speedy = sy / time
        speedx = sx / time
    if random.random() >= 0.8:
        speedy /= 2
        speedx /= 2
    else:
        speedx /= 3
        speedy /= 3
    speeds.append(speedx)
    speeds.append(speedy)
    return speeds


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.lives = random.randrange(1, 5)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WALL_SIZE + self.rect.width, WIDTH - WALL_SIZE - self.rect.width)
        self.rect.y = random.randrange(WALL_SIZE + self.rect.height, HEIGHT - WALL_SIZE - self.rect.height)
        self.spawn_time = pygame.time.get_ticks() + random.randrange(0, 5000)
        self.changed_speed_time = pygame.time.get_ticks()
        self.speedx = random.randrange(-5, 5)
        self.speedy = random.randrange(-5, 5)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        time = pygame.time.get_ticks()
        # Ходьба мобов
        draw_text(screen, str(self.lives), 30, self.rect.x, self.rect.y)
        if self.changed_speed_time == self.spawn_time:
            self.changed_speed_time += 5000
        if time - self.changed_speed_time >= random.randrange(2000, 4000):
            if random.random() >= 0.9:
                self.speedx = 0
                self.speedy = 0
            elif random.random() >= 0.7:
                self.speedx = to_player_go(self)[0]
                self.speedy = to_player_go(self)[1]
            else:
                self.speedx = random.randrange(-5, 5)
                self.speedy = random.randrange(-5, 5)
            self.changed_speed_time = time
        # Проверка выхода за карту
        if self.rect.right >= WIDTH - WALL_SIZE:
            self.speedx *= -1
        if self.rect.left <= 0 + WALL_SIZE:
            self.speedx *= -1
        if self.rect.top <= 0 + WALL_SIZE:
            self.speedy *= -1
        if self.rect.bottom >= HEIGHT - WALL_SIZE:
            self.speedy *= -1

# Спрайты
mobs = pygame.sprite.Group()