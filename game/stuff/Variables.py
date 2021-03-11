import math

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Настройка окна
screen_name = 'ahahaha'
WIDTH = 1500
HEIGHT = 1000
FPS = 60

# Для мобов
# Значения для спавна мобов
mobs_values_x = []
mobs_values_y = []
for i in range(50, WIDTH - 50):
    mobs_values_x.append(i)
for i in range(50, HEIGHT - 50):
    mobs_values_y.append(i)
