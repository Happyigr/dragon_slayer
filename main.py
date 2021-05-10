import pygame
from classes.Mob import *
from classes.Sword import *
from classes.Sword_hit import *
from classes.Abilities import *
from classes.Teleport import *
from classes.Coin import *
from classes.Player import *
from classes.Wall import *
from stuff.Map import *
from stuff.Menu import *
global all_money


# Убийство моба с выпадением монеток кол-во которых зависит от названия моба (small, big...)
def mob_kill(mob):
    if mob.type == 'small':
        coin_mob_drop(mob.rect.centerx, mob.rect.centery, 1, 5)
        mob.kill()
    if mob.type == 'medium':
        coin_mob_drop(mob.rect.centerx, mob.rect.centery, 5, 10)
        mob.kill()
    if mob.type == 'big':
        coin_mob_drop(mob.rect.centerx, mob.rect.centery, 10, 20)
        mob.kill()


# Если есть абилка в ability то можно таким образом передать сюда название абилки и сброситься её кд
def ability_reload_show(time, name):
    for abil in abilites_sprites:
        if abil.ability_name == name:
            abil.reloaded = False
            abil.last_time_used = time


# Дроп монеток с мобов с максимальным и минимальным значением
def coin_mob_drop(x, y, min, max):
    coin_amount = random.randrange(min, max)
    for coin in range(coin_amount):
        newcoin(x, y)


# Выбор меча по атрибуту sword.chosen
def sword_choose():
    global sword
    if not len(sword_sprites) == 0:
        for i in sword_sprites:
            i.kill
    for i in item_sprites:
        if i.chosen:
            sword = Sword(i.damage, i.rate)
            sword_sprites.add(sword)
            all_sprites.add(sword)
    return sword


# Инициализация карты игры
def map_init():
    for x, y in walls_coord:
        wall = Wall(x, y)
        wall_sprites.add(wall)
        all_sprites.add(wall)


# Вызывает скрин нового уровня и спавнит новых мобов (не убивая старых мобов!!!!)
def new_lvl(mobs, lvl):
    show_lvl_screen(lvl)
    player.rect.center = (WIDTH / 2, HEIGHT - WALL_SIZE - 50)
    for wall in wall_sprites:
        wall.kill()
    for i in range(mobs):
        newmob()
    for teleport in teleport_sprites:
        teleport.hide()
    for coin in coins_sprites:
        coin.kill()
    map_init()


# Спавн монетки
def newcoin(x, y):
    coin = Coin(x, y)
    all_sprites.add(coin)
    coins_sprites.add(coin)


# Спавн моба (координаты присваиваются случайно, если их не указали)
def newmob(centerx=None, centery=None):
    if centerx is None and centery is None:
        # seq_num из Map.py
        cell_num = random.randrange(0, seq_num - 1)
        centerx = spawn_coord_x[cell_num]
        centery = spawn_coord_y[cell_num]
    m = Mob(centerx, centery)
    all_sprites.add(m)
    mobs.add(m)


# Спавн удар меча (и сам класс Superhit преследует меч)
def sword_hit_ability():
    hit = Sword_hit()
    sword_hit_sprites.add(hit)
    all_sprites.add(hit)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(screen_name)
clock = pygame.time.Clock()

# Спрайты
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(teleport1)
all_sprites.add(teleport2)
all_sprites.add(teleport3)
all_sprites.add(speedboost)
all_sprites.add(superhit)


# Цикл игры
all_money = 500
running = True
game_over = True
# Чтобы первый меч был в начале игры всегда активен
sword_1_item.chosen = True
sword_1_item.buyed = True
while running:
    time = pygame.time.get_ticks()
    screen.fill(BLACK)
    if game_over:
        lvl_num = 1
        all_money = show_menu_screen(all_money)
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
                if player.SPEEDBOOST_RELOAD:
                    ability_reload_show(time, 'speedboost')
                    player.speedboost()
            if event.key == pygame.K_ESCAPE:
                game_over = show_setting_screen(all_money)
            for teleport in teleport_sprites:
                if event.key == pygame.K_e and teleport.isOver():
                    lvl_num += 1
                    new_lvl(8, lvl_num)


    # Столкновения спрайтов
    # Проверка не ударил ли меч моба
    hits = pygame.sprite.spritecollide(sword, mobs, False)
    if hits:
        for hit in hits:
            if time - sword.last_hit >= sword.rate:
                sword.last_hit = time
                hit.lives -= sword.damage
                if hit.lives <= 0:
                    mob_kill(hit)

    # Проверка не ударил ли супер хит мобов
    for sword_hit in sword_hit_sprites:
        hits = pygame.sprite.spritecollide(sword_hit, mobs, False)
        if hits:
            for hit in hits:
                sword.last_hit = time
                hit.lives -= sword.damage
                if hit.lives <= 0:
                    mob_kill(hit)

    # Проверка не ударил ли моб игрока
    hits = pygame.sprite.spritecollide(player, mobs, True)
    if hits:
        for hit in hits:
            player.lives -= 1
            if player.lives == 0:
                game_over = True

    # Проверка не ударился ли моб со стеной
    hits = pygame.sprite.groupcollide(mobs, wall_sprites, False, False)
    if hits:
        for hit in hits:
            hit.speed = (hit.speed[0] * -1, hit.speed[1] * -1)

    # Остальное
    # Убить спрайт суперудара после того как время удара прошло
    if time - player.SUPERHIT_TIMEON >= player.SUPERHIT_DURATION:
        for sword_superhit in sword_hit_sprites:
            sword_superhit.kill()

    # Проверка сбора монеток игроком
    hits = pygame.sprite.spritecollide(player, coins_sprites, True)
    for coin in hits:
        all_money += coin.cost

    # Показать телепорт после убийства всех мобов
    for teleport in teleport_sprites:
        if len(mobs) == 0 and teleport.hidden:
            teleport.unhide()
        # Проверка не стоит ли игрок в портале
        if teleport.isOver() and not teleport.hidden:
            draw_text(screen, 'Нажми Е, чтобы войти в портал', 30, WIDTH / 2, HEIGHT / 2)

    # Обновление
    all_sprites.update()
    # Рендеринг
    draw_text(screen, 'Меню на ESC', 30, 120, HEIGHT - 50)
    draw_text(screen, (str(all_money) + ' $'), 30, 120, HEIGHT - 100)
    draw_lives(screen, WIDTH - 100, 30, player.lives, heart_image)
    all_sprites.draw(screen)
    pygame.display.update()
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
