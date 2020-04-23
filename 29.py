"""
Знайти кількість парних елементів одновимірного масиву до першого
зустрінутого числа рівного наперед заданому числу а.
Васильченко Даниїл Назарович 122А
"""
import numpy as np

# Введення стоп-числа та массиву
a = int(input("Введіть стоп-число: "))
input_massive = list(np.array([int(input(f"Введіть число: "))
                    for i in range(int(input("Введіть довжину масиву: ")))]))
if a in input_massive:
    input_massive = input_massive[:input_massive.index(a)]
    # Виведення масиву та кількості парних елементів зрізаного масиву
    print("Ваш зрізаний до *a* масив: ", input_massive)
    print(f"Кількість парних елементів: {sum(((i % 2) == 0) for i in input_massive)}")
else:
    print("Вашего числа немає в послідовності")