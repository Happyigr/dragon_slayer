import random
import pygame
from stuff.Settings import *
from stuff.Button import *
from stuff.Methods import *
from img.images import *
from stuff.Map import *


def ability_reload_show(time, name):
    for abil in abilites_sprites:
        if abil.ability_name == name:
            abil.reloaded = False
            abil.last_time_used = time


def sword_hit_ability():
    hit = Sword_hit()
    sword_hit_sprites.add(hit)
    all_sprites.add(hit)


def sword_choose():
    if not len(sword_sprites) == 0:
        for i in sword_sprites:
            i.kill
    for i in item_sprites:
        if i.chosen:
            sword = Sword(i.damage, i.rate)
            sword_sprites.add(sword)
            all_sprites.add(sword)
    return sword


def show_setting_screen():
    setting = True
    while setting:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        screen.fill(BLACK)
        draw_text(screen, 'Настройки', 40, WIDTH / 2, 80)
        for button in setting_buttons:
            button.draw(screen)
            if button.isOver(mouse):
                button.color = (DARK_BUTTON)
            else:
                button.color = (WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in setting_buttons:
                    if button.isOver(mouse):
                        if button == back_button_setting:
                            setting = False
                        if button == in_menu_button_settings:
                            setting = False
                            return True  # game over == True
                        if button == exit_button_all:
                            quit()

        pygame.display.flip()


def swords_in_shop(item, num):
    global all_money_gl
    if item.num == num:
        if item_array[num - 1].buyed:
            for sword in item_sprites:
                sword.chosen = False
            item_array[num - 1].chosen = True
        if not item_array[num - 1].buyed and all_money_gl >= item_array[num - 1].cost:
            all_money_gl -= item_array[num - 1].cost
            item_array[num - 1].buyed = True
        if not item_array[num - 1].buyed and all_money_gl <= item_array[num - 1].cost:
            no_money = True
            while no_money:
                mouse = pygame.mouse.get_pos()
                clock.tick(FPS)
                screen.fill(BLACK)
                no_money_button_shop.draw(screen)
                draw_text(screen, 'Не хватает денег', 30, WIDTH / 2, HEIGHT / 2)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if no_money_button_shop.isOver(mouse):
                            no_money = False
                    if no_money_button_shop.isOver(mouse):
                        no_money_button_shop.color = (DARK_BUTTON)
                    else:
                        no_money_button_shop.color = (WHITE)
                pygame.display.flip()


def show_shop_screen():
    shop = True
    while shop:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        screen.fill(BLACK)
        item_sprites.draw(screen)
        item_sprites.update()
        draw_text(screen, 'Чтобы купить товар, нажми на него', 30, WIDTH / 2, HEIGHT - 200)
        draw_text(screen, (str(all_money_gl) + ' $'), 30, WIDTH / 2, 30)
        draw_text(screen, 'Магазин', 56, WIDTH / 2, 100)
        draw_text(screen, 'Урон', 30, 150, 414)
        draw_text(screen, 'Уд/с', 30, 150, 464)
        for button in shop_buttons:
            button.draw(screen)
        for event in pygame.event.get():
            for button in shop_buttons:
                if button.isOver(mouse):
                    button.color = (DARK_BUTTON)
                else:
                    button.color = (WHITE)
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Выбор предмета
                for item in item_sprites:
                    if item.isOver(mouse):
                        for num in range(len(item_array) + 1):
                            swords_in_shop(item, num)
                for button in shop_buttons:
                    if button.isOver(mouse):
                        if button == back_button_shop:
                            shop = False
        pygame.display.flip()


def show_menu_screen():
    waiting = True
    while waiting:
        clock.tick(FPS)
        screen.fill(BLACK)
        draw_text(screen, (str(all_money_gl) + ' $'), 30, WIDTH / 2, 30)
        draw_text(screen, "Dragon Slayer", 64, WIDTH / 2, 100)
        for button in menu_buttons:
            button.draw(screen)
        mouse = pygame.mouse.get_pos()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            for button in menu_buttons:
                if button.isOver(mouse):
                    button.color = (DARK_BUTTON)
                else:
                    button.color = (WHITE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in menu_buttons:
                    if button.isOver(mouse):
                        if button == exit_button_all:
                            quit()
                        if button == info_button_menu:
                            show_info_screen()
                        if button == upgrade_button_menu:
                            show_shop_screen()
                        if button == play_button_menu:
                            waiting = False
        pygame.display.flip()


def show_info_screen():
    info = True
    while info:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        screen.fill(BLACK)
        draw_text(screen, 'Правила', 50, WIDTH / 2, HEIGHT / 2 - 100)
        draw_text(screen, 'Меч бегает за крусором, ты должен убивать им всех врагов.', 30, WIDTH / 2, HEIGHT / 2)
        draw_text(screen, 'Одновременно ты (герой) должен уворачиваться от врагов', 30, WIDTH / 2, HEIGHT / 2 + 50)
        draw_text(screen, 'У тебя есть суперспособность которая увеличивает скорость твоего героя на 3 секунды',
                  30, WIDTH / 2, HEIGHT / 2 + 100)
        draw_text(screen, 'Для применения нажми на ЛКМ', 30, WIDTH / 2, HEIGHT / 2 + 150)
        draw_text(screen, 'версия игры: 0.0.0.6', 25, WIDTH / 2, HEIGHT - 40)
        for button in info_buttons:
            button.draw(screen)
        for event in pygame.event.get():
            for button in info_buttons:
                if button.isOver(mouse):
                    button.color = (DARK_BUTTON)
                else:
                    button.color = (WHITE)
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in info_buttons:
                    if button.isOver(mouse):
                        if button == back_button_info:
                            info = False
        pygame.display.flip()


def show_lvl_screen(lvl):
    screen.fill(BLACK)
    draw_text(screen, str('Уровень ' + str(lvl)), 100, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, 'Q для start', 50, WIDTH / 2, HEIGHT - 100)
    pygame.display.flip()
    lvl = True
    while lvl:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    lvl = False


def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


def new_lvl(mobs, lvl):
    show_lvl_screen(lvl)
    player.rect.center = (WIDTH / 2, HEIGHT - WALL_SIZE - 50)
    for i in range(mobs):
        newmob()
    for teleport in teleport_sprites:
        teleport.hide()
    for coin in coins_sprites:
        coin.kill()


def newcoin(x, y):
    coin = Coin(x, y)
    all_sprites.add(coin)
    coins_sprites.add(coin)


def coin_mob_drop(x, y):
    coin_amount = random.randrange(1, 5)
    for coin in range(coin_amount):
        coin_x = random.randrange(-50, 50) + x
        coin_y = random.randrange(-50, 50) + y
        newcoin(coin_x, coin_y)


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
        #Поворот по х и у
        time = 30
        Sx = player.rect.centerx - mouse_x
        Sy = player.rect.centery - mouse_y
        self.speedx = Sx / time
        self.speedy = Sy / time


class Sword_hit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1000, 1000))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = sword.rect.centerx
        self.rect.centery = sword.rect.centery

    def update(self):
        self.rect.centerx = sword.rect.centerx
        self.rect.centery = sword.rect.centery


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

    # Возвращает координаты в виде x y
    def get_coord(self):
        coord = [self.rect.x, self.rect.y]
        return coord


class Abilities(pygame.sprite.Sprite):
    def __init__(self, img, x, y, reload_time, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.image_orig = img
        self.ability_name = name
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.last_time_used = 0
        self.reload_time = reload_time
        self.reloaded = True

    def update(self):
        time = pygame.time.get_ticks()
        if not self.reloaded:
            reload = round(self.reload_time / 1000 - (time / 1000 - self.last_time_used / 1000), 1)
            self.image = pygame.Surface((0, 0))
            draw_text(screen, str(reload), 30, self.rect.centerx, self.rect.centery)
            if reload <= 0:
                self.reloaded = True
        else:
            self.image = self.image_orig


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        if random.random() >= 0.8:
            self.image = pygame.Surface((20, 20))
            self.image.fill(YELLOW)
            self.cost = 10
        elif random.random() >= 0.5:
            self.image = pygame.Surface((15, 15))
            self.image.fill(GREY)
            self.cost = 5
        else:
            self.image = pygame.Surface((10, 10))
            self.image.fill(BROWN)
            self.cost = 1
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        if self.rect.right >= WIDTH - WALL_SIZE:
            self.rect.right = WIDTH - WALL_SIZE
        if self.rect.left <= 0 + WALL_SIZE:
            self.rect.left = 0 + WALL_SIZE
        if self.rect.top <= 0 + WALL_SIZE:
            self.rect.top = 0 + WALL_SIZE
        if self.rect.bottom >= HEIGHT - WALL_SIZE:
            self.rect.bottom = HEIGHT - WALL_SIZE

    def update(self):
        pass


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


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(screen_name)
clock = pygame.time.Clock()

# Кнопки
setting_buttons = []
menu_buttons = []
info_buttons = []
shop_buttons = []
exit_button_all = Button(WHITE, ((WIDTH / 2) - 100), HEIGHT - 100, 200, 50, 'Выход', 30)
# Кнопки Настроек
back_button_setting = Button(WHITE, ((WIDTH / 2) - 100), HEIGHT - 250, 200, 50, 'Продолжить', 30)
in_menu_button_settings = Button(WHITE, ((WIDTH / 2) - 100), HEIGHT - 175, 200, 50, 'В меню', 30)
# Кнопки меню
play_button_menu = Button(WHITE, ((WIDTH / 2) - 100), HEIGHT - 325, 200, 50, 'Играть', 30)
upgrade_button_menu = Button(WHITE, ((WIDTH / 2) - 100), HEIGHT - 250, 200, 50, 'Улучшение', 30)
info_button_menu = Button(WHITE, ((WIDTH / 2) - 100), HEIGHT - 175, 200, 50, 'Инфо', 30)
# Кнопки для магазина
no_money_button_shop = Button(WHITE, ((WIDTH / 2) - 100), HEIGHT - 100, 200, 50, 'Ок', 30)
back_button_shop = Button(WHITE, ((WIDTH / 2) - 100), HEIGHT - 100, 200, 50, 'Назад', 30)
# Кнопки для инфо
back_button_info = Button(WHITE, ((WIDTH / 2) - 100), HEIGHT - 100, 200, 50, 'Назад', 30)

# Товары
sword_1_item = Item_sword(armor_1_img, 300, 300, 0, 1, 1000, 1)
sword_2_item = Item_sword(armor_2_img, 450, 300, 100, 2, 700, 2)
sword_3_item = Item_sword(armor_3_img, 600, 300, 300, 3, 500, 3)
sword_4_item = Item_sword(armor_4_img, 750, 300, 500, 1, 200, 4)
item_sprites = pygame.sprite.Group()
item_array = []
item_array.append(sword_1_item)
item_array.append(sword_2_item)
item_array.append(sword_3_item)
item_array.append(sword_4_item)
item_sprites.add(sword_1_item)
item_sprites.add(sword_2_item)
item_sprites.add(sword_3_item)
item_sprites.add(sword_4_item)

# Добавление кнопок в списки
setting_buttons.append(exit_button_all)
setting_buttons.append(back_button_setting)
setting_buttons.append(in_menu_button_settings)
menu_buttons.append(exit_button_all)
menu_buttons.append(info_button_menu)
menu_buttons.append(play_button_menu)
menu_buttons.append(upgrade_button_menu)
shop_buttons.append(back_button_shop)
info_buttons.append(back_button_info)

# Спрайты
sword_hit_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
sword_sprites = pygame.sprite.Group()
teleport_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
coins_sprites = pygame.sprite.Group()
player = Player()

# Телепорты
teleport1 = Teleport(WIDTH / 2, 50 + WALL_SIZE)
teleport2 = Teleport(100 + WALL_SIZE, HEIGHT / 2)
teleport3 = Teleport(WIDTH - 100 - WALL_SIZE, HEIGHT / 2)
teleport_sprites.add(teleport1)
teleport_sprites.add(teleport2)
teleport_sprites.add(teleport3)
all_sprites.add(player)
all_sprites.add(teleport1)
all_sprites.add(teleport2)
all_sprites.add(teleport3)

# Способности
abilites_names = ['speedboost', 'superhit']
abilites_sprites = pygame.sprite.Group()
speedboost = Abilities(speedboost_img_mini, 75, 75, player.SPEEDBOOST_RELOADTIME, 'speedboost')
superhit = Abilities(superhit_img_mini, 150, 75, player.SUPERHIT_RELOADTIME, 'superhit')
abilites_sprites.add(superhit)
abilites_sprites.add(speedboost)
all_sprites.add(speedboost)
all_sprites.add(superhit)

# Цикл игры
new_lvl_time = 0
running = True
game_over = True
sword_1_item.chosen = True
sword_1_item.buyed = True
while running:
    time = pygame.time.get_ticks()
    screen.fill(BLACK)
    if game_over:
        lvl_num = 1
        show_menu_screen()
        sword = sword_choose()
        for i in mobs.sprites():
            i.kill()
        new_lvl(8, lvl_num)
        player.lives = 3
        player.SPEEDBOOST_TIMEON = 0
        game_over = False
    # Держим цикл на правильной скорости
    time = pygame.time.get_ticks()
    clock.tick(FPS)
    # убить спрайт суперудара после того как время удара прошло
    if time - player.SUPERHIT_TIMEON >= player.SUPERHIT_DURATION:
        for sword_superhit in sword_hit_sprites:
            sword_superhit.kill()
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        # Суперудар
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player.SUPERHIT_RELOAD:
                ability_reload_show(time, 'superhit')
                player.SUPERHIT_RELOAD = False
                player.SUPERHIT_TIMEON = time
                sword_hit_ability()
        # Настройки
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                ability_reload_show(time, 'speedboost')
                player.speedboost()
            if event.key == pygame.K_ESCAPE:
                game_over = show_setting_screen()
            for teleport in teleport_sprites:
                if event.key == pygame.K_e and teleport.isOver():
                    lvl_num += 1
                    new_lvl_time = time
                    new_lvl(8, lvl_num)

    # Проверка не ударил ли меч моба
    hits = pygame.sprite.spritecollide(sword, mobs, False)
    for hit in hits:
        if time - sword.last_hit >= sword.rate:
            sword.last_hit = time
            hit.lives -= sword.damage
            if hit.lives <= 0:
                hit.kill()
                coin_mob_drop(hit.rect.centerx, hit.rect.centery)

    # Проверка не ударил ли супер хит мобов
    for sword_hit in sword_hit_sprites:
        hits = pygame.sprite.spritecollide(sword_hit, mobs, False)
        for hit in hits:
            sword.last_hit = time
            hit.lives -= sword.damage
            if hit.lives <= 0:
                hit.kill()
                coin_mob_drop(hit.rect.centerx, hit.rect.centery)

    # Проверка не ударил ли моб игрока
    if time - new_lvl_time:
        hits = pygame.sprite.spritecollide(player, mobs, True)
        for hit in hits:
            player.lives -= 1
            if player.lives == 0:
                game_over = True

    # Проверка сбора монеток игроком
    hits = pygame.sprite.spritecollide(player, coins_sprites, True)
    for hit in hits:
        all_money_gl += hit.cost

    # Создание портала
    for teleport in teleport_sprites:
        if len(mobs) == 0 and teleport.hidden:
            teleport.unhide()
        # Проверка не стоит ли игрок в портале
        if teleport.isOver() and not teleport.hidden:
            draw_text(screen, 'Нажми Е, чтобы войти в портал', 30, WIDTH / 2, HEIGHT / 2)

    # Обновление
    all_sprites.update()
    # Рендеринг
    for x, y in world_map:
        pygame.draw.rect(screen, GREY, (x, y, WALL_SIZE, WALL_SIZE), 2)
    draw_text(screen, 'Меню на ESC', 30, 120, HEIGHT - 50)
    draw_text(screen, (str(all_money_gl) + ' $'), 30, 120, HEIGHT - 100)
    draw_lives(screen, WIDTH - 100, 30, player.lives, heart_image)
    all_sprites.draw(screen)
    pygame.display.update()
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
