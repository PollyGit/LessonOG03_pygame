import random

import pygame  #импортируем библиотеку
import randint from random

pygame.init()  #инициализируем библиотеку


# создание констант в ветке part-constant-code
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#переменная, где создается экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#задаем название нашего созданного окна с помощью ф-ции display
pygame.display.set_caption('Игра ТИР')
#создание иконки
icon = pygame.image.load('image/icon_tir.png')
#устанавливаем иконку
pygame.display.set_icon(icon)


#создание объекта, по которому будем стрелять, его параметры
target_image = pygame.display.load('image/target_tir.png')  #(с сайта klipartz)
target_width = 50
target_height = 50
#Задаем рандомные координаты x,y появления цели.
#Вычитаем, чтобы цель не оказалась за экраном и вся поместилась
#от 0 до ширины/высоты экрана минус ширина/высота цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
#переменная цвета для заливки фона окна
color = (random.randint(0, 255), random.randint(0, 255),random.randint(0, 255))





#создание игрового цикла, в данном случае while
running = True
while True:
    pass

pygame.quit()  #закрывает окно с игрой, когда цикл завершится