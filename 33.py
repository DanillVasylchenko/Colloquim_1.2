"""
Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
Васильченко Даниїл Назарович 122А
"""
import numpy as np

# Введення масиву
input_massive = np.array([int(input(f"Введіть число: "))
                          for i in range(1, 21)])
print("Ваш масив: ", input_massive)
# пошук ненульових елементів та добуток їх
kek = 1
for i in input_massive:
    if i != 0:
        kek *= 1
if kek == 1:
    print("Лише нулики у масиві")
else:
    print("Добуток чисел масиву")