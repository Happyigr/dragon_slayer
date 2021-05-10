from stuff.Button import *
from classes.Item_sword import *
import pygame


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(screen_name)
clock = pygame.time.Clock()


def show_setting_screen(money):
    setting = True
    while setting:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        screen.fill(BLACK)
        draw_text(screen, (str(money) + ' $'), 30, 120, HEIGHT - 100)
        draw_text(screen, 'Настройки', 40, WIDTH / 2, 80)
        for button in setting_buttons:
            button.draw(screen)
            if button.isOver(mouse):
                button.color = DARK_BUTTON
            else:
                button.color = WHITE
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


def swords_in_shop(item, num, money):
    if item.num == num:
        if item_array[num - 1].buyed:
            for sword in item_sprites:
                sword.chosen = False
            item_array[num - 1].chosen = True
        if not item_array[num - 1].buyed and money >= item_array[num - 1].cost:
            money -= item_array[num - 1].cost
            item_array[num - 1].buyed = True
        if not item_array[num - 1].buyed and money <= item_array[num - 1].cost:
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
                        no_money_button_shop.color = DARK_BUTTON
                    else:
                        no_money_button_shop.color = WHITE
                pygame.display.flip()
    return money


def show_shop_screen(money):
    shop = True
    while shop:
        clock.tick(FPS)
        mouse = pygame.mouse.get_pos()
        screen.fill(BLACK)
        item_sprites.draw(screen)
        item_sprites.update()
        draw_text(screen, 'Чтобы купить товар, нажми на него', 30, WIDTH / 2, HEIGHT - 200)
        draw_text(screen, (str(money) + ' $'), 30, WIDTH / 2, 30)
        draw_text(screen, 'Магазин', 56, WIDTH / 2, 100)
        draw_text(screen, 'Урон', 30, 150, 414)
        draw_text(screen, 'Уд/с', 30, 150, 464)
        for button in shop_buttons:
            button.draw(screen)
        for event in pygame.event.get():
            for button in shop_buttons:
                if button.isOver(mouse):
                    button.color = DARK_BUTTON
                else:
                    button.color = WHITE
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Выбор предмета
                for item in item_sprites:
                    if item.isOver(mouse):
                        for num in range(len(item_array) + 1):
                            money = swords_in_shop(item, num, money)
                for button in shop_buttons:
                    if button.isOver(mouse):
                        if button == back_button_shop:
                            shop = False
        pygame.display.flip()
    return money


def show_menu_screen(money):
    waiting = True
    while waiting:
        clock.tick(FPS)
        screen.fill(BLACK)
        draw_text(screen, (str(money) + ' $'), 30, WIDTH / 2, 30)
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
                    button.color = DARK_BUTTON
                else:
                    button.color = WHITE
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in menu_buttons:
                    if button.isOver(mouse):
                        if button == exit_button_all:
                            quit()
                        if button == info_button_menu:
                            show_info_screen()
                        if button == upgrade_button_menu:
                            money = show_shop_screen(money)
                        if button == play_button_menu:
                            waiting = False
        pygame.display.flip()
    return money


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
        draw_text(screen, 'версия игры: 0.0.0.12', 25, WIDTH / 2, HEIGHT - 40)
        for button in info_buttons:
            button.draw(screen)
        for event in pygame.event.get():
            for button in info_buttons:
                if button.isOver(mouse):
                    button.color = DARK_BUTTON
                else:
                    button.color = WHITE
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
