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
    'W.............W',
    'W....WWWWWWWWWW',
    'W.............W',
    'W.............W',
    'W.............W',
    'WWWWWWWWWWWWWWW',
]

walls_coord = []
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            walls_coord.append((i * WALL_SIZE, j * WALL_SIZE))
