"""
Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
від 50 до 100.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
from random import randint

# Введення массиву та числа
input_massive = np.array([randint(50, 100) for i in range(10)])
input_number = int(input("Введіть число: "))
# Виведення масиву та добутку елементів
print("Ваш масив: ", input_massive)
kek = 1
for i in input_massive:
    if i > input_number:
        kek *= i
if kek != 1:
    print("Добуток елементів : ", kek)
else:
    print("Немає елементів, що менше 0!")
