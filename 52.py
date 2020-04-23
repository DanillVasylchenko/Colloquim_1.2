"""
Знайти найбільший елемент з елементів одновимірного масиву, що мають
парний номер. Визначити, чи є він єдиним.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
# Введення масиву
input_massive = np.array([int(input("Введіть елемент: ")) for i in range(int(input("Введіть кількість елементів: ")))])
print("Ваш масив: ", input_massive)
list = [input_massive[i] for i in range(0, len(input_massive), 2)] # кроком 2 створюєм список із парними індеками
max = max(list)
if list.count(max) == 1:
    print("Максимальний елемент єдиний")
else:
    print("Максимальний елемент не єдиний")