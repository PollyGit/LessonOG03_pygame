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

# Переменные для подсчета очков и времени
score = 0
last_move_time = pygame.time.get_ticks()
move_interval = 2000  # Интервал перемещения в миллисекундах

# Переменные для нового объекта
moving_object_image = pygame.image.load('image/dove_tir80.png')
moving_object_image_width = 50
moving_object_image_height = 50
#moving_object_image = pygame.Surface((30, 30))
#moving_object_image.fill((255, 0, 0))
moving_object_x = None
moving_object_y = random.randint(0, SCREEN_HEIGHT - 50)
moving_object_speed = 1
last_object_spawn_time = pygame.time.get_ticks()
spawn_interval = random.randint(2000, 5000)  # 10-20 секунд


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
                # Увеличение очков
                score += 1
                #снова выдаем рандомные координаты
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    # Автоматическое перемещение цели каждые 2 секунды
    current_time = pygame.time.get_ticks()
    if current_time - last_move_time > move_interval:
        target_x = random.randint(0, SCREEN_WIDTH - target_width)
        target_y = random.randint(0, SCREEN_HEIGHT - target_height)
        last_move_time = current_time
    # Появление и движение нового объекта
    if moving_object_x is None and current_time - last_object_spawn_time > spawn_interval:
        # Определяем, с какой стороны появится объект
        if random.choice([True, False]):
            moving_object_x = 0  # Появляется слева
            moving_object_speed = 1
        else:
            moving_object_x = SCREEN_WIDTH - 50  # Появляется справа
            moving_object_speed = -1
        moving_object_y = random.randint(0, SCREEN_HEIGHT - 50)
        last_object_spawn_time = current_time
        spawn_interval = random.randint(2000, 5000)  # Обновляем интервал появления

    if moving_object_x is not None:
        moving_object_x += moving_object_speed
        screen.blit(moving_object_image, (moving_object_x, moving_object_y))
        # Проверяем, не вышел ли объект за пределы экрана
        if moving_object_x < -50 or moving_object_x > SCREEN_WIDTH:
            moving_object_x = None  # Удаляем объект

    #указываем отрисовку объекта target_image и его координаты
    screen.blit(target_image, (target_x, target_y))
    # Отрисовка очков
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Очки: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    #ВАЖНО! Для обновления экрана, тк в игре все происходит покадрово
    pygame.display.update()


pygame.quit()  #закрывает окно с игрой, когда цикл завершится