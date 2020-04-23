"""
Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому
повторюється найчастіше число.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
# Введення масиву
input_massive = list(np.array([int(input("Введіть число: ")) for i in range(int(input("Введіть довжину масиву: ")))]))
print("Ваш масив: ", input_massive)

# Перетворивши список у множину і використавши метод count для знаходження числа входжень елемента в список, отримуємо:
num = max(set(input_massive), key=input_massive.count)

print(f"Стільки разів повторюється найчастіше число {num}: ", input_massive.count(num))