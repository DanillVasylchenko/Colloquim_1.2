"""
Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність
масиву - 15. Заповнення масиву здійснити випадковими числами від 10 до 50.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
from random import randint

# Введення массиву
input_massive = np.array([randint(10, 50) for i in range(15)])

# Виведення масиву та добутку кратних 7 елементів
print("Ваш масив: ", input_massive)
kek = 1
for i in input_massive:
    if i % 7 == 0:
        kek *= i
if kek != 1:
    print("Добуток елементів кратних 7: ", kek)
else:
    print("Немає елементів, що кратні 7!")