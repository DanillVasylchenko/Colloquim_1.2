"""
Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10.
Заповнення масиву здійснити випадковими числами від 5 до 500.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
from random import randint

# Введення массиву
input_massive = np.array([randint(5, 500) for i in range(10)])
# Виведення масиву та добутку елементів
print("Ваш масив: ", input_massive)
kek = 1
for i in input_massive:
    if i % 3 == 0 and i % 9 == 0:
        kek *= i
if kek != 1:
    print("Добуток елементів : ", kek)
else:
    print("Немає елементів, що кратні 9 та 3 одночасно!")