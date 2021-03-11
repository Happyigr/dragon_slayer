# images by Dan Sevenstar -DontMind8-

from stuff.Variables import *
from os import path
import pygame

# Создание игры и окна
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The best game ever')
clock = pygame.time.Clock()

# Путь к папке с картинками
img_dir = path.join(path.dirname(__file__))

# Картинки
sword_img = pygame.image.load(path.join(img_dir, 'sword_golden.png')).convert()
sword_img_mini = pygame.transform.scale(sword_img, (30, 54))
heart_image = pygame.Surface((20, 20))
heart_image.fill(RED)
