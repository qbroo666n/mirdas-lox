# import random

# def guess_color():
#     colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']
#     chosen_color = random.choice(colors)
    
#     print("Угадай цвет!")
#     while True:
#         guess = input("Введите свое предположение: ").strip().lower()
#         if guess == chosen_color:
#             print("Поздравляю! Вы угадали правильный цвет.")
#             break
#         else:
#             print("Неверное предположение. Попробуйте еще раз!")

# if __name__ == "__main__":
#     guess_color()

# import pygame
# import sys
# import random

# pygame.init()


# width, height = 600, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Угадай цвет!")

# COLOR = {
    
# "red": (255, 0, 0),
# "green": (0, 255, 0),
# "blue": (0, 0, 255),
# "yellow": (255, 255, 0),
# "cyan": (0, 255, 255),
# "magenta": (255, 0, 255),
# "white": (255, 255, 255),
# "black": (0, 0, 0),
# "silver": (192, 192, 192),
# "gray": (128, 128 , 128),
# "gold": (225, 215, 0),
# "coral": (255, 127, 80),
# }

# color_keys = list(COLOR.keys())
# current_color = random.choice(color_keys)

# # Основной игровой цикл
# while True: # бесконечный цикл
#     for event in pygame.event.get(): # Обработка событий
#         if event.type == pygame.QUIT:  # Закрытие окна
#             pygame.quit()  # Выход из Pygame
#             sys.exit()  # Выход из программы

#         if event.type == pygame.KEYDOWN:  # Проверка нажатия клавиши
#             # Изменение цвета фона при нажатии любой клавиши
#             if event.key == pygame.K_r:  # Если нажата 'R'
#                 current_color = "RED"
#             elif event.key == pygame.K_g:  # Если нажата 'G'
#                 current_color = "GREEN"
#             elif event.key == pygame.K_b:  # Если нажата 'B'
#                 current_color = "BLUE"
#             elif event.key == pygame.K_y:  # Если нажата 'Y'
#                 current_color = "YELLOW"
#             elif event.key == pygame.K_c:  # Если нажата 'C'
#                 current_color = "CYAN"
#             elif event.key == pygame.K_m:  # Если нажата 'M'
#                 current_color = "MAGENTA"
#             elif event.key == pygame.K_w:  # Если нажата 'W'
#                 current_color = "WHITE"
#             elif event.key == pygame.K_k:  # Если нажата 'K'
#                 current_color = "BLACK"
#             elif event.key == pygame.K_n:  # Если нажата 'n'
#                 current_color = "siver"
#             elif event.key == pygame.K_g:  # Если нажата 'g'
#                 current_color = "gold"
#             elif event.key == pygame.K_c:  # Если нажата 'c'
#                 current_color = "coral"


#     # Заливка экрана текущим цветом
#     screen.fill(COLOR[current_color])

#     # Обновление экрана
#     pygame.display.flip()

# Игра угадай цвет

import pygame # библиотека для создание игр
import sys # для графики
import random # для генераций случайны чисел

# Инициляция Py game

pygame.init()

width, height = 600,600 # размер окна
screen = pygame.display.set_mode((width,height)) # выбор размера оокна
pygame.display.set_caption("Угадай цвет братишка") #  заголовок окна
# Цветы
COLOR = {
    "RED" : (255,0,0),
    "GREEN" : (0,255,0),
    "BLUE" : (255,0,255),
    "YELLOW" : (255,255,0),
    "CYAN" : (0,255,255),
    "MAGENTA": (255,0,255),
    "WHITE" : (255,255,255),
    "BLACK" : (0,0,0),
    "TEAL" : (0,128,128),
    "PUPLE" : (128,0,128),
    "SILVER": (192, 192, 192),
}
color_keys = list(COLOR.keys())
current_color = random.choice(color_keys)
# Основной игровой цикл
while True: # бесконечный цикл
    for event in pygame.event.get(): # Обработка событий
        if event.type == pygame.QUIT:  # Закрытие окна
            pygame.quit()  # Выход из Pygame
            sys.exit()  # Выход из программы

        if event.type == pygame.KEYDOWN:  # Проверка нажатия клавиши
            # Изменение цвета фона при нажатии любой клавиши
            if event.key == pygame.K_r:  # Если нажата 'R'
                current_color = "RED"
            elif event.key == pygame.K_g:  # Если нажата 'G'
                current_color = "GREEN"
            elif event.key == pygame.K_b:  # Если нажата 'B'
                current_color = "BLUE"
            elif event.key == pygame.K_y:  # Если нажата 'Y'
                current_color = "YELLOW"
            elif event.key == pygame.K_c:  # Если нажата 'C'
                current_color = "CYAN"
            elif event.key == pygame.K_m:  # Если нажата 'M'
                current_color = "MAGENTA"
            elif event.key == pygame.K_w:  # Если нажата 'W'
                current_color = "WHITE"
            elif event.key == pygame.K_k:  # Если нажата 'K'
                current_color = "BLACK"
            elif event.key == pygame.K_t:  # Если нажата 'T'
                current_color = "TEAL"
            elif event.key == pygame.K_a:  # Если нажата 'A'
                current_color = "PUPLE"
            elif event.key == pygame.K_o:  # Если нажата 'o'
                current_color = "SILVER"
           



    # Заливка экрана текущим цветом
    screen.fill(COLOR[current_color])

    # Обновление экрана
    pygame.display.flip()