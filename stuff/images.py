# images by Dan Sevenstar -DontMind8-

from stuff.Settings import *
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
sword_img = pygame.image.load(path.join(img_dir, '../img/sword_golden.png')).convert()
sword_img_mini = pygame.transform.scale(sword_img, (30, 54))
heart_image = pygame.Surface((20, 20))
heart_image.fill(RED)
speedboost_img = pygame.image.load(path.join(img_dir, '../img/10.png'))
speedboost_img_mini = pygame.transform.scale(speedboost_img, (75, 75))
superhit_img = pygame.image.load(path.join(img_dir, '../img/13.png'))
superhit_img_mini = pygame.transform.scale(superhit_img, (75, 75))
armor_1_img = pygame.image.load(path.join(img_dir, '../img/18.png'))
armor_2_img = pygame.image.load(path.join(img_dir, '../img/19.png'))
armor_3_img = pygame.image.load(path.join(img_dir, '../img/20.png'))
armor_4_img = pygame.image.load(path.join(img_dir, '../img/17.png'))
wall_img = pygame.image.load(path.join(img_dir, '../img/wall.png'))
player_img = pygame.Surface((50, 50))
