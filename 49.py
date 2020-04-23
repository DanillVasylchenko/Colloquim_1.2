"""
Задано дві таблиці. Одна містить найменування послуг, а інша - розцінки
за ці послуги. Видаліть з обох таблиць все, що передує послузі, ціна якої G гривень.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
print("Введіть назву послуги та ціну через пробіл або натисніть Enter для завершення: ")
input_table = [] # майбутня таблиця
while True:
    a = input("Послуга та ціна: ")
    if len(a) == 0:
        break
    input_table.append(a.split(" "))
G = input("Введіть ціну для зрізу: ")
for i in range(len(input_table)):
    if G in input_table[i]:
        input_table = input_table[i:]
        break
for i in range(len(input_table)):
    print(f"Послуга: {input_table[i][0]} Ціна: {int(input_table[i][1])}")