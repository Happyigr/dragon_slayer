import pygame
from game.stuff.Settings import *

# W = стена
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

wall_colision = []
world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * WALL_SIZE, j * WALL_SIZE))
            wall_colision.append(pygame.Rect(i * WALL_SIZE, j * WALL_SIZE, WALL_SIZE, WALL_SIZE))