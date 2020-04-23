"""
Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5.
Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами від 10 до
100.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
from random import randint

# Введення массиву
input_massive = np.array([randint(10, 100) for i in range(10)])
# Виведення масиву та добутку елементів
print("Ваш масив: ", input_massive)
kek = 1
for i in input_massive:
    if i % 5 == 0:
        kek *= i
if kek != 1:
    print("Добуток елементів : ", kek)
else:
    print("Немає елементів, що кратні 10!")