"""
Знайти суму всіх елементів масиву цілих чисел, які менше середнього
арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
здійснити випадковими числами від 150 до 300.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
from random import randint

# Введення массиву
input_massive = np.array([randint(150, 300) for i in range(20)])
# Виведення масиву та суми елементів які менше середнього арифметичного масиву
print("Ваш масив: ", input_massive)
kek = 0
arithmetic_average = input_massive.mean()
for i in input_massive:
    if i < arithmetic_average:
        kek += i
print("Сума елементів, які менше середнього арифметичного масиву: ", kek)
