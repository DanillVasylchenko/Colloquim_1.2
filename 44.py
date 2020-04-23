"""
Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
своїм номером і при цьому кратні 3..
Васильченко Даниїл Назарович 122А
"""
import numpy as np

# Введення масиву
input_massive = np.array([int(input(f"Введіть число: "))
                          for i in range(int(input(f"Введіть довжину масиву: ")))])
print("Ваш масив: ", input_massive)
count = 0  # кількість елементів що задовільняють умові
count_index = 0  # лічильник індексів
for i in input_massive:
    if i == count_index and i % 3 == 0:
        count += 1
    count_index += 1
print("Кількість елементів, що задовільняють умові: ", count)
