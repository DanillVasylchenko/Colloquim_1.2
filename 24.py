"""
Знайти суму елементів масиву цілих чисел, які діляться на 5 і на 8
одночасно. Розмірність масиву - 30. Заповнення масиву здійснити випадковими
числами від 500 до 1000.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
from random import randint
# Введення массиву
input_massive = np.array([randint(500, 1000) for i in range(30)])
# Виведення масиву та суми елементів
print("Ваш масив: ", input_massive)
kek = 0
for i in input_massive:
    if i % 5 == 0 and i % 8 == 0:
        kek += i
print("Сума елементів : ", kek)