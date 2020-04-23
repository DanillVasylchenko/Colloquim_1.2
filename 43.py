"""
Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b.
Васильченко Даниїл Назарович 122А
"""
import numpy as np

# Введення масиву
input_massive = np.array([int(input(f"Введіть число: "))
                          for i in range(int(input(f"Введіть довжину масиву: ")))])
print("Ваш масив: ", input_massive)
a, b = int(input("Введіть число a: ")), int(input("Введіть число b: "))
for i in input_massive:
    if i % a == 0 and i % b != 0:
        w = True
        print(w)
        break