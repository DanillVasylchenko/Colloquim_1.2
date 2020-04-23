"""
Знайти суму всіх елементів масиву дійсних чисел, більших за задане
число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
від 50 до 100.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
from random import randint

# Введення массиву та числа
input_massive = np.array([randint(50, 100) for i in range(20)])
input_number = int(input("Введіть число: "))
# Виведення масиву та суми елементів остача від ділення яких на 2 дорівнює 3
print("Ваш масив: ", input_massive)
kek = 0
for i in input_massive:
    if i > input_number:
        kek += i
print("Сума елементів, більших за задане Вами: ", kek)
