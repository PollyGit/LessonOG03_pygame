import pygame  #импортируем библиотеку

pygame.init()  #инициализируем библиотеку

# создание констант в ветке part-constant-code
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#переменная, где создается экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#задаем название нашего созданного окна
pygame.display.set_caption('Игра ТИР')
#создание иконки
icon = pygame.image.load('')


#создание игрового цикла, в данном случае while
running = True
while True:
    pass

pygame.quit()  #закрывает окно с игрой, когда цикл завершится