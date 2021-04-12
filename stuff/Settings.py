import math


# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_BUTTON = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (220, 220, 220)
BROWN = (221, 153, 102)

# Настройка окна
screen_name = 'ahahaha'
WIDTH = 1500
HEIGHT = 1000
FPS = 60
WALL_SIZE = 100

# Для мобов
# Значения для спавна мобов
mobs_values_x = []
mobs_values_y = []
mobs_values_player_spawn_x = []
mobs_values_player_spawn_y = []
for i in range(50, WIDTH - 50):
    mobs_values_x.append(i)
for i in range(50, HEIGHT - 200):
    mobs_values_y.append(i)
