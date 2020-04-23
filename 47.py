"""
У лінійному масиві знайти максимальний елемент. Вставте порядковий
номер елемента за ним, пересунувши всі залишилися на одну позицію вправо.
Васильченко Даниїл Назарович 122А
"""
import numpy as np

# Введення масиву
input_massive = list(np.array([int(input("Введіть число: "))
                           for i in range(int(input("Введіть довжину масиву: ")))]))
print("Ваш масив: ", input_massive)
max = max(input_massive)
print("Максимальний елемент: ", max)
# вставляємо перед максимальним числом число що позначає індекс
input_massive.insert(input_massive.index(max) - 1, input_massive.index(max))
print("Оновлений масив: ", input_massive)
