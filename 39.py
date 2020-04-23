"""
Дані про температуру повітря і кількості опадів за декаду квітня
зберігаються в масивах. Визначити кількість опадів, що випали у вигляді дощу і у
вигляді снігу за цю декаду.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
from random import randint

# За прогнозом синоптиків, місячна кількість опадів очікується 24-50 мм,
# що в межах середніх багаторічних значень.

# Введення масиву температур та опадів(під час квітня може статись Великий Вибух)
input_massive_temp = np.array([randint(-272, 142000000000000000000000000000000) for i in range(10)])
input_massive_opadi = np.array([randint(2, 5) for i in range(10)])
print(f"Масив температур повітря: {input_massive_temp},"
      f"Масив опадів: {input_massive_opadi}")
rain = 0
snow = 0
count = 0
for i in input_massive_temp:
    if i <= 0:
        snow += input_massive_opadi[count]
    else:
        rain += input_massive_opadi[count]
    count += 1
print(f"Кількть дощу {rain}мм\n"
      f"Кількість снігу {snow}мм")