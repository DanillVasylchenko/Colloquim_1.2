"""
Знайти суму парних елементів масиву цілих чисел. Розмірність масиву -
20. Заповнення масиву здійснити випадковими числами від 100 до 200.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
from random import randint

# Введення массиву
input_massive = np.array([randint(100, 200) for i in range(20)])

# Виведення масиву та суми парних елементів масиву
print("Ваш масив: ", input_massive)
sum = 0
for i in input_massive:
    if i % 2 == 0:
        sum += i
print("Сума парних елементів: ", sum)