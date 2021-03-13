import random
import pygame
from stuff.Button import *
from stuff.Methods import *
from img.images import *


def map_save():
    pass


def show_setting_screen():
    setting = True
    screen.fill(BLACK)
    draw_text(screen, 'Настройки', 40, WIDTH / 2, 80)
    for button in setting_buttons:
        button.draw(screen, WHITE)
    pygame.display.flip()
    while setting:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            for button in setting_buttons:
                if button.isOver(mouse) and button == exit_button and event.type == pygame.MOUSEBUTTONDOWN:
                    quit()
                if button.isOver(mouse) and button == back_button and event.type == pygame.MOUSEBUTTONDOWN:
                    setting = False
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                pass


def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


def show_lvl_screen(lvl):
    screen.fill(BLACK)
    draw_text(screen, str('Уровень ' + str(lvl)), 100, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, 'Q для start', 50, WIDTH / 2, HEIGHT - 100)
    pygame.display.flip()
    lvl = True
    while lvl:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    lvl = False


def show_go_screen():
    screen.fill(BLACK)
    draw_text(screen, "Dragon Slayer", 64, WIDTH / 2, 100)
    draw_text(screen, 'Правила', 50, WIDTH / 2, HEIGHT / 2 - 100)
    draw_text(screen, 'Меч бегает за курсором, ты должен убивать им всех врагов.', 30, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, 'Одновременно ты (герой) должен уворачиваться от врагов', 30, WIDTH / 2, HEIGHT / 2 + 50)
    draw_text(screen, 'У тебя есть суперспособность которая увеличивает скорость твоего героя на 3 секунды',
              30, WIDTH / 2, HEIGHT / 2 + 100)
    draw_text(screen, 'Для применения нажми на ЛКМ', 30, WIDTH / 2, HEIGHT / 2 + 150)
    draw_text(screen, 'Нажми пробел для того чтобы начать игру.', 40, WIDTH / 2, HEIGHT - 100)
    pygame.display.flip()
    waiting = True
    while waiting:
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False


def new_lvl(mobs, lvl):
    show_lvl_screen(lvl)
    player.rect.center = (WIDTH / 2, HEIGHT - 50)
    for i in range(mobs):
        newmob()
    for teleport in teleport_sprites:
        teleport.hide()


def random_no_0(start, stop):
    time = 0
    while time == 0:
        time = random.randrange(start, stop)
    return time


# не нужно
def teleport_spawn(x, y):
    portal = Teleport(x, y)
    portal.add(all_sprites)
    portal.add(teleport_sprites)


# Скорость для движения к игроку в виде x y
def to_player_go(mob):
    speeds = []
    time = 30
    Sx = player.get_coord()[0] - mob.get_coord()[0]
    Sy = player.get_coord()[1] - mob.get_coord()[1]
    speedx = Sx / time
    speedy = Sy / time
    while not (-5 <= speedx <= 5) and not (-5 <= speedy <= 5) and speedy == 0 and speedx == 0:
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
        self.rect.center = (WIDTH / 2, HEIGHT - 50)
        self.speed = 5
        self.lives = 3
        self.immune_time = 3000
        self.SPEEDBOOST_TIMEON = 0
        self.SPEEDBOOST_TIME = 3000
        self.SPEEDBOOST_RELOAD = True
        self.SPEEDBOOST_RELOADTIME = 5000
        self.SPEEDBOOST_ON = False

    def update(self):
        key_event = pygame.key.get_pressed()
        left = key_event[pygame.K_a]
        right = key_event[pygame.K_d]
        straight = key_event[pygame.K_w]
        back = key_event[pygame.K_s]
        if left:
            self.rect.x -= self.speed
        if right:
            self.rect.x += self.speed
        if straight:
            self.rect.y -= self.speed
        if back:
            self.rect.y += self.speed
        # Проверка выхода за карту
        if self.rect.right >= WIDTH - 50:
            self.rect.right = WIDTH - 50
        if self.rect.left <= 0 + 50:
            self.rect.left = 0 + 50
        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
        if self.rect.top <= 0 + 50:
            self.rect.top = 0 + 50
        # Способности
        # Проверка на перезарядку спидбуста
        if time - self.SPEEDBOOST_TIMEON >= self.SPEEDBOOST_RELOADTIME:
            self.SPEEDBOOST_RELOAD = True
        if time - self.SPEEDBOOST_TIMEON > self.SPEEDBOOST_TIME:
            self.speed = 5
            self.SPEEDBOOST_ON = False

    def hit(self):
        pass

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
        self.rect.centerx = mouse_x
        self.rect.centery = mouse_y
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


class Teleport(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image.fill(BLUE)
        self.image_orig = self.image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.hidden = False
        self.y_orig = y
        self.x_orig = x

    def update(self):
        pass

    def isOver(self):
        if self.rect.left <= player.rect.centerx <= self.rect.right and \
                self.rect.bottom >= player.rect.centery >= self.rect.top:
            return True

    def hide(self):
        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()
        self.hidden = True

    def unhide(self):
        self.image = self.image_orig
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x_orig
        self.rect.y = self.y_orig
        self.hidden = False


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


class Abilities(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.image_orig = img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        reload = 5 - int((int(time - player.SPEEDBOOST_TIMEON)) / 1000)
        if not player.SPEEDBOOST_RELOAD:
            self.image = pygame.Surface((0, 0))
            draw_text(screen, str(reload), 30, self.rect.centerx, self.rect.centery)
        else:
            self.image = self.image_orig


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(screen_name)
clock = pygame.time.Clock()

# Спрайты
all_sprites = pygame.sprite.Group()
sword_sprite = pygame.sprite.Group()
teleport_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
sword = Sword()
teleport1 = Teleport(WIDTH / 2, 50)
teleport2 = Teleport(100, HEIGHT / 2)
teleport3 = Teleport(WIDTH - 100, HEIGHT / 2)
sword_sprite.add(sword)
teleport_sprites.add(teleport1)
teleport_sprites.add(teleport2)
teleport_sprites.add(teleport3)
all_sprites.add(player)
all_sprites.add(sword)
all_sprites.add(teleport1)
all_sprites.add(teleport2)
all_sprites.add(teleport3)

# Способности
abilites_sprites = pygame.sprite.Group()
speedboost = Abilities(speedboost_img_mini, 75, 75)
abilites_sprites.add(speedboost)
all_sprites.add(speedboost)

# Кнопки
setting_buttons = []
exit_button = Button(WHITE, ((WIDTH / 2) - 100), HEIGHT - 100, 200, 50, 'Выход', 30)
back_button = Button(WHITE, ((WIDTH / 2) - 100), HEIGHT - 175, 200, 50, 'Назад', 30)
setting_buttons.append(exit_button)
setting_buttons.append(back_button)

# Цикл игры
new_lvl_time = 0
running = True
game_over = True
while running:
    time = pygame.time.get_ticks()
    screen.fill(BLACK)
    if game_over:
        lvl_num = 1
        show_go_screen()
        for i in mobs.sprites():
            i.kill()
        new_lvl(8, lvl_num)
        player.lives = 3
        player.SPEEDBOOST_TIMEON = 0
        game_over = False
    # Держим цикл на правильной скорости
    time = pygame.time.get_ticks()
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        # Удар
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.speedboost()
        # Настройки
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                show_setting_screen()

    # Проверка не убил ли меч моба
    hits = pygame.sprite.groupcollide(mobs, sword_sprite, True, False, pygame.sprite.collide_circle)
    for hit in hits:
        pass

    # Проверка не ударил ли моб игрока
    if time - new_lvl_time > player.immune_time:
        hits = pygame.sprite.spritecollide(player, mobs, True)
        for hit in hits:
            player.lives -= 1
            if player.lives == 0:
                game_over = True

    # Создание портала
    for teleport in teleport_sprites:
        if len(mobs) == 0 and teleport.hidden:
            teleport.unhide()
        # Проверка не стоит ли игрок в портале
        if teleport.isOver() and not teleport.hidden:
            lvl_num += 1
            new_lvl_time = time
            new_lvl(8, lvl_num)

    # Обновление
    all_sprites.update()
    # Рендеринг
    draw_text(screen, 'Меню на ESC', 30, 120, HEIGHT - 50)
    draw_lives(screen, WIDTH - 100, 30, player.lives, heart_image)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
