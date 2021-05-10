from stuff.Methods import *
# settings есть в Methods


def random_map_create():
    pass

# W = стена
# Комната 15 на 9 (1500 на 900)
text_map = [
    'WWWWWWWWWWWWWWW',
    'W.............W',
    'W.............W',
    'W.............W',
    'W........W....W',
    'W.............W',
    'W....WW...WW..W',
    'W.............W',
    'W.............W',
    'WWWWWWWWWWWWWWW',
]

# Назначаем каждой клетке номер и ищем стены, добавляем координаты верхнего левого угла стен в список
# чтобы было удобно создавать стены.(так как у спрайта x0 и y0 = левый верхний угол)
# j = номер строчки, i = номер столбца, row = строка
walls_coord = []
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            walls_coord.append((i * WALL_SIZE, j * WALL_SIZE))
spawn_coord_x = {}
spawn_coord_y = {}
seq_num = 0
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == '.':
            # В словаре координаты середины клеток без стен, подписанные номером
            spawn_coord_x[seq_num] = (i * WALL_SIZE + WALL_SIZE / 2)
            spawn_coord_y[seq_num] = (j * WALL_SIZE + WALL_SIZE / 2)
            seq_num += 1
