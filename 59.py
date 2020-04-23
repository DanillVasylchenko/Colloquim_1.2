"""
Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних
чисел в ньому.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
# Введення масиву
input_massive = np.array([int(input("Введіть число: ")) for i in range(10)])
print("Ваш масив: ", input_massive)
print("К-ть різних чисел: ", len(set(input_massive)))