"""
Створіть масив А [1..7] за допомогою генератора випадкових чисел і
виведіть його на екран. Збільште всі його елементи в 2 рази.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
from random import randint

# параметри рандому
start = int(input("Введіть найменше можливе число: "))
stop = int(input("Введіть найбільше можливе число: "))
# генерація масиву
input_massive = np.array([randint(start, stop) for i in range(7)])
# виведемо масив та його версію де всі елементи поножені на 2
print("Ваш масив: ", input_massive)
print("Ваш масив з елементами помноженими на 2: ", np.array([i * 2 for i in input_massive]))