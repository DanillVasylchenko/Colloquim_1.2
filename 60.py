"""
Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число
однакових чисел, що йдуть підряд в ньому.
Васильченко Даниїл Назарович 122А
"""
import numpy as np

# Введення масиву
input_massive = np.array([int(input("Введіть число: ")) for i in range(10)])
print("Ваш масив: ", input_massive)
count = 1  # рахівничка для послідовностей однакових елементів (вважитимемо що 1 це взагалі входження елемента в масив)
count_final = 0  # рахівничка для найбільшої послідовності однакових чисел
for i in input_massive:
    for j in range(1, len(input_massive)):
        if i == input_massive[j]:
            count += 1
            if count > count_final:
                count_final = count
        else:
            count = 0
print("Найбільше число однакових чисел", count_final)