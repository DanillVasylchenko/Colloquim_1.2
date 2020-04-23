"""
Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які потрапляють в інтервал від -2 до 10.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
# Введення масиву
input_massive = list(np.array([int(input(f"Введіть число: "))
                          for i in range(int(input("Введіть довжину масиву: ")))]))
print("Ваш масив: ", input_massive)
# проходимо по елементам та видаляем ті, що не належать інтервалу
for i in input_massive:
    if i not in range(-2, 11):
        input_massive.remove(i)
print(f"Масив без зайвих елементів: {np.array(input_massive)}\n"
      f"Середнє арифметичне значення елементів: {np.array(input_massive).mean()}")