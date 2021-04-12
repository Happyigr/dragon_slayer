from stuff.Methods import *
# settings есть в Methods

# W = стена
# Комната 15 на 9 (1500 на 900)
text_map = [
    'WWWWWWWWWWWWWWW',
    'W.............W',
    'W.............W',
    'W.............W',
    'W.............W',
    'W.............W',
    'W.............W',
    'W.............W',
    'W.............W',
    'WWWWWWWWWWWWWWW',
]

walls_coord = []
world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            walls_coord.append((i * WALL_SIZE, j * WALL_SIZE))
