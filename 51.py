"""
Дан одновимірний масив а. Сформувати новий масив, який складається
тільки з тих елементів масиву а, які перевищують свій номер на 10. Якщо таких
елементів немає, то видати повідомлення.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
# Введення масиву
input_massive = np.array([int(input("Введіть елемент: ")) for i in range(int(input("Введіть кількість елементів: ")))])
print("Ваш масив: ", input_massive)
future_massive = []
index_count = 0
for i in input_massive:
    if i - index_count == 10: #перевірка задоволення умови
        future_massive.append(i)
    index_count += 1
if len(future_massive) > 0:
    print("Новий масив: ", np.array(future_massive))
else:
    print("Немає елементів вашего масиву що задовільняють умову!")