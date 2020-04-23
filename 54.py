"""
Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
однаковими значеннями.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
# Введення масиву
input_massive = sorted(np.array([int(input("Введіть число: ")) for i in range(20)]))
print("Ваш масив: ", input_massive)
input_massive_2 = set(input_massive) # set залишає лише унікальні елементи
if len(input_massive) == len(input_massive_2):
    print("Елементів з однаковими значеннями немає")
else:
    print("Елементи з однаковими значеннями є")