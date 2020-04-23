"""
Якщо в одновимірному масиві є три поспіль однакових елемента, то
змінній r привласнити значення істина.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
# Введення масиву
input_massive = np.array([int(input("Введіть число: ")) for i in range(int(input("Введіть довжину масиву: ")))])
print("Ваш масив: ", input_massive)
count = 0 # рахівничка для однакових елементів
for i in range(len(input_massive)):
    if input_massive[i] == input_massive[i + 1] or input_massive[i] == input_massive[i - 1]:
        count += 1
    if count == 3:
        r = True
        print(r)
        break