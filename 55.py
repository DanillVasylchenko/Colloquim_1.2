"""
У будинку, що складається з 30 квартир, переселити мешканців так, щоб
мешканці першої квартири переїхали в тридцяту, з тридцятого - в першу, з другої - в 29
і т.д., знайдіть кількість квартир, в яких проживає більше 5 осіб.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
# Введення масиву
input_massive = np.array([int(input("Введіть кількість мешканців: ")) for i in range(30)])
print("Ваш масив: ", input_massive)
print("Переселення: ", input_massive[::-1])
print("Кількість квартир з більше ніж 5 людей: ", sum(filter(lambda x: x > 5, input_massive)))