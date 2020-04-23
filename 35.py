"""
Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
спаданню.
Васильченко Даниїл Назарович 122А
"""
import numpy as np

# Введення масиву

input_massive = np.array(
    [int(input(f"Введіть число масиву: ")) for i in range(int(input(f"Введіть довжину масиву: ")))])
print("Ваш масив: ", input_massive)

if len(input_massive) == 1:
    print("Лише одне число!")
else:
    # перевірка чи є даний масив рівний його відсортований за спаданням, якщо буде хоч одна перестановка,
    # то це означатиме що алгоритм з самого початку невідсортований за спаданням
    def bubbleSort(arr):
        flag = False
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag = True
                    break
        return flag
    if bubbleSort(input_massive):
        print("Масив неупорядкований за спаданням")
    else:
        print("Масив упорядкований за спаданням")