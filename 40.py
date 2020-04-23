"""
Обчислити суму парних елементів одновимірного масиву до першого
зустрінутого нульового елемента.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
from random import randint

# Введення масиву
input_massive = list(np.array([int(input(f"Введіть число: "))
                               for i in range(int(input(f"Введіть довжину масиву: ")))]))
print("Ваш масив: ", input_massive)
if 0 in input_massive:
    input_massive = input_massive[:input_massive.index(0)]
# виводимо суму парних  елементів
print(sum(filter(lambda x: x % 2 == 0, input_massive)))
