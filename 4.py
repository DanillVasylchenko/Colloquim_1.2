"""
Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
починаються з певної букви, яка вводиться з клавіатури.
Васильченко Даниїл Назарович 122А
"""
import numpy as np


# вводимо потрібну першу літеру та вивиодимо всі елементи з масиву у яких найперший елемент є введеною літерою
letter = input("Введіть першу літеру: ")[:1]
for el in np.array([input('Введіть прізвище: ') for i in range(5)]):
    if el[0] == letter:
        print(el)


