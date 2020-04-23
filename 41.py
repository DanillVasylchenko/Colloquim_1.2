"""
Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
# підрахунок елементів
from collections import Counter

# Введення масиву
input_massive = np.array([int(input(f"Введіть число: "))
                               for i in range(int(input(f"Введіть довжину масиву: ")))])
a = int(input("Введіть число, з ким буде порівнюватись максимальний елемент: "))
print("Ваш масив: ", input_massive)
counter = Counter(input_massive)
max = input_massive.max()
if counter[max] == 1 and max <= a:
    t = True
    print(t)
else:
    print(False)