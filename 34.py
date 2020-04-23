"""
Дано два лінійних масиву однакової розмірності. Скласти третій масив з
добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.
Васильченко Даниїл Назарович 122А
"""
import numpy as np

# Введення масиву
massive_length = int(input("Введіть довжину масивів: "))
input_massive_1 = np.array([int(input(f"Введіть число 1-го масиву: "))
                            for i in range(massive_length)])
input_massive_2 = np.array([int(input(f"Введіть число 2-го масиву: "))
                            for i in range(massive_length)])
print("Ваш 1-й масив: ", input_massive_1)
print("Ваш 2-й масив: ", input_massive_2)
massive_3 = input_massive_1 * input_massive_2
print("Третій масив: ", massive_3)
