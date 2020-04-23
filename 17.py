"""
Знайти суму елементів масиву дійсних чисел, що мають непарні номери.
Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100
до 200
Васильченко Даниїл Назарович 122А
"""
import numpy as np
from random import randint

# Введення массиву
input_massive = np.array([randint(100, 200) for i in range(20)])

# Виведення масиву та сума елементів з непарними номерами
print("Ваш масив: ", input_massive)
kek = 0
for i in range(1, len(input_massive), 2):
        kek += input_massive[i]
print("Сума елементів, що мають непарні номери: ", kek)
