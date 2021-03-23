from game.classes.Mob import *
from game.classes.Sword import *
from game.classes.Sword_hit import *
from game.classes.Abilities import *
from game.classes.Teleport import *
from game.classes.Coin import *
from game.classes.Player import *
from stuff.Map import *
from stuff.Menu import *
global all_money


# Сбрасывает кд абилки по имени
def ability_reload_show(time, name):
    for abil in abilites_sprites:
        if abil.ability_name == name:
            abil.reloaded = False
            abil.last_time_used = time


def coin_mob_drop(x, y, min, max):
    coin_amount = random.randrange(min, max)
    for coin in range(coin_amount):
        coin_x = random.randrange(-50, 50) + x
        coin_y = random.randrange(-50, 50) + y
        newcoin(coin_x, coin_y)


def sword_hit_ability():
    hit = Sword_hit()
    sword_hit_sprites.add(hit)
    all_sprites.add(hit)


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
                game_over = show_setting_screen(all_money)
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
                if hit.name == 'small':
                    coin_mob_drop(hit.rect.centerx, hit.rect.centery, 1, 5)
                    hit.kill()
                if hit.name == 'medium':
                    coin_mob_drop(hit.rect.centerx, hit.rect.centery, 5, 10)
                    hit.kill()
                if hit.name == 'big':
                    coin_mob_drop(hit.rect.centerx, hit.rect.centery, 10, 20)
                    hit.kill()

    # Проверка не ударил ли супер хит мобов
    for sword_hit in sword_hit_sprites:
        hits = pygame.sprite.spritecollide(sword_hit, mobs, False)
        for hit in hits:
            sword.last_hit = time
            hit.lives -= sword.damage
            if hit.lives <= 0:
                if hit.name == 'small':
                    coin_mob_drop(hit.rect.centerx, hit.rect.centery, 1, 5)
                    hit.kill()
                if hit.name == 'medium':
                    coin_mob_drop(hit.rect.centerx, hit.rect.centery, 5, 10)
                    hit.kill()
                if hit.name == 'big':
                    coin_mob_drop(hit.rect.centerx, hit.rect.centery, 10, 20)
                    hit.kill()

    # Проверка не ударил ли моб игрока
    if time - new_lvl_time:
        hits = pygame.sprite.spritecollide(player, mobs, True)
        for mob in hits:
            player.lives -= 1
            if player.lives == 0:
                game_over = True

    # Проверка сбора монеток игроком
    hits = pygame.sprite.spritecollide(player, coins_sprites, True)
    for coin in hits:
        all_money += coin.cost

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
    draw_text(screen, (str(all_money) + ' $'), 30, 120, HEIGHT - 100)
    draw_lives(screen, WIDTH - 100, 30, player.lives, heart_image)
    all_sprites.draw(screen)
    pygame.display.update()
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
