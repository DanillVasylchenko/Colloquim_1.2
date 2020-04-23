"""
Розсортуйте заданий лінійний масив по зростанню.
Васильченко Даниїл Назарович 122А
"""
import numpy as np

# Введення масиву

input_massive = np.array(
    [int(input(f"Введіть число масиву: ")) for i in range(int(input(f"Введіть довжину масиву: ")))])
print("Ваш масив: ", input_massive)


# сортування бульбашками
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print("Сортування бульбашкою за зростанням: ", bubbleSort(input_massive))
