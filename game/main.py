import random
import pygame
import math
from stuff.Methods import *
from img.images import *

def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


def random_no_0(start, stop):
    time = 0
    while time == 0:
        time = random.randrange(start, stop)
    return time


# Скорость для движения к игроку в виде x y
def to_player_go(mob):
    speeds = []
    time = 30
    Sx = player.get_coord()[0] - mob.get_coord()[0]
    Sy = player.get_coord()[1] - mob.get_coord()[1]
    speedx = Sx / time
    speedy = Sy / time
    while not (-5 <= speedx <= 5) and not(-5 <= speedy <= 5) and speedy == 0 and speedx == 0:
        time += 5
        speedy = Sy / time
        speedx = Sx / time
    if random.random() >= 0.8:
        speedy /= 2
        speedx /= 2
    else:
        speedx /= 3
        speedy /= 3
    speeds.append(speedx)
    speeds.append(speedy)
    return speeds


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
        pass

    # Возвращает координаты в виде x y
    def get_coord(self):
        coord = [self.rect.x, self.rect.y]
        return coord


class Sword(pygame.sprite.Sprite):
    def __init__(self):
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
        self.damage = None
        self.range = None
        self.angle = 0

    def update(self):
        # ходьба меча
        mouse_coord = pygame.mouse.get_pos()
        mouse_x = mouse_coord[0]
        mouse_y = mouse_coord[1]
        if -30 <= mouse_x - self.rect.centerx <= 30:
            self.speedx = 0
        elif self.rect.centerx <= mouse_x:
            self.speedx += 5
        elif self.rect.centerx >= mouse_x:
            self.speedx += -5
        if -30 <= mouse_y - self.rect.centery <= 30:
            self.speedy = 0
        elif self.rect.centery <= mouse_y:
            self.speedy += 5
        elif self.rect.centery >= mouse_y:
            self.speedy += -5
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Проверка на выход за пределы
        if self.rect.right >= WIDTH - 50:
            self.rect.right = WIDTH - 50
        if self.rect.left <= 0 + 50:
            self.rect.left = 0 + 50
        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
        if self.rect.top <= 0 + 50:
            self.rect.top = 0 + 50

    def hit(self):
        pass

    # не работает
    def rotate(self):
        mouse_coord = pygame.mouse.get_pos()
        mouse_x = mouse_coord[0]
        mouse_y = mouse_coord[1]
        # Поворот меча
        self.angle = 0
        max_x = 0
        max_y = 0
        if mouse_x >= self.rect.x:
            max_x = mouse_x
        else:
            max_x = self.rect.x
        if mouse_y >= self.rect.y:
            max_y = mouse_y
        else:
            max_y = self.rect.y
        dx = max_x - abs(mouse_x - self.rect.x)
        dy = max_y - abs(mouse_y - self.rect.y)
        tan = dy / dx
        self.angle = int(tan * 180 / math.pi)
        # Определение в какой четверти курсор
        ddx = mouse_x - self.rect.x
        ddy = mouse_y - self.rect.y
        # 1 четверть
        if ddx >= 0 and ddy >= 0:
            self.angle += 0
        # 2 четверть
        if ddx <= 0 and ddy >= 0:
            self.angle += 90
        # 3 четверть
        if ddx <= 0 and ddy <= 0:
            self.angle += 180
        # 4 четверть
        if ddx >= 0 and ddy <= 0:
            self.angle += 270
        print(self.angle)
        self.image = pygame.transform.rotate(self.image_orig, self.angle)


class Sword_hit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 30))


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(mobs_values_x)
        self.rect.y = random.choice(mobs_values_y)
        self.spawn_time = pygame.time.get_ticks() + random.randrange(0, 5000)
        self.changed_speed_time = pygame.time.get_ticks()
        self.speedx = random.randrange(-5, 5)
        self.speedy = random.randrange(-5, 5)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        time = pygame.time.get_ticks()
        # Ходьба мобов
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
        if self.rect.right >= WIDTH - 50:
            self.rect.right = WIDTH - 50
            self.speedx = self.speedx * -1
        if self.rect.left <= 0 + 50:
            self.rect.left = 0 + 50
            self.speedx = self.speedx * -1
        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.speedy = self.speedy * -1
        if self.rect.top <= 0 + 50:
            self.rect.top = 0 + 50
            self.speedy = self.speedy * -1

    # Возвращает координаты в виде x y
    def get_coord(self):
        coord = [self.rect.x, self.rect.y]
        return coord


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(screen_name)
clock = pygame.time.Clock()

# Спрайты
all_sprites = pygame.sprite.Group()
sword_sprite = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
sword = Sword()
sword_sprite.add(sword)
all_sprites.add(player)
all_sprites.add(sword)

# Цикл игры
for i in range(8):
    newmob()
running = True
while running:
    # Спавн меча и Работа с ним
    #sword.rect.midbottom = player.rect.midtop
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        # Удар
        if event.type == pygame.MOUSEBUTTONDOWN:
            sword.hit()

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
