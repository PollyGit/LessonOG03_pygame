import random

import pygame  #импортируем библиотеку
from random import randint

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
target_image = pygame.image.load('image/target_tir.png')  #(с сайта klipartz)
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
while running:
    #заливка цветом
    screen.fill(color)
    #отслеживание всех событий в игре с помощью цикла for
    #event - переменная, которая будет содержать список всех событий
    #pygame.event.get() получить все события, представлены в виде коллекции
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #условие завершения цикла for, нажатие на крестик
            running = False
        #нажатие на кнопку мыши и определение, в каком месте она нажата, координаты
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # попала ли в область цели
            if target_x < mouse_x < (target_x +target_width) and target_y < mouse_y < (target_y +target_height):
                #снова выдаем рандомные координаты
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    #указываем отрисовку объекта target_image и его координаты
    screen.blit(target_image, (target_x, target_y))
    #ВАЖНО! Для обновления экрана, тк в игре все происходит покадрово
    pygame.display.update()


pygame.quit()  #закрывает окно с игрой, когда цикл завершится