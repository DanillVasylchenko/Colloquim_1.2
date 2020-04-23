"""
Підрахувати кількість елементів одновимірного масиву, для яких
виконується нерівність i*i<ai<i!
Васильченко Даниїл Назарович 122А
"""
# вважатимемо і як індекс
import numpy as np
from math import factorial

# Введення масиву
input_massive = list(np.array([int(input(f"Введіть число: "))
                               for i in range(int(input(f"Введіть довжину масиву: ")))]))
print("Ваш масив: ", input_massive)

print("Кількість разів виконання рівності (i*i<ai<i!): ",
      sum(input_massive.index(a) ** 2 < a < factorial(input_massive.index(a)) for a in input_massive))
