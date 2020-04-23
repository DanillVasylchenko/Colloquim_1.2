"""
Створіть масив з 15 цілочисельних елементів і визначте серед них
мінімальне значення.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
from random import randint

# Введення массиву
min, max = int(input("Введіть мінімальне рандомне значення: ")), int(input("Введіть мінімальне рандомне значення: "))
input_massive = np.array([randint(min, max) for i in range(10)])

# Виведення масиву та мінімального значення
print("Ваш масив: ", input_massive)
print("Мінімальне значення: ", input_massive.min())