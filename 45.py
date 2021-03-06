"""
Перетин даху має форму півкола з радіусом R м. Сформувати таблицю,
яка містить довжини опор, які встановлюються через кожні R / 5 м.
Васильченко Даниїл Назарович 122А
"""
import math

# трикутник, утворений точкою на колі і кінцями діаметру є прямокутний,
# а висота, опущена з прямого кута є середнє геометричне відрізків діаметра, на які вона його ділить
R = int(input('Введіть радіус: '))

opori_taken_distance = R / 5  # скільки метрів зайнято опорами
opora_count = 0  # кількість опор
opora_index = 0  # порядковий номер опори

while opora_count < (2 * R - opori_taken_distance):  # щоб не вийти за межі діаметру півкола(даху)
    opora_count += opori_taken_distance
    opora_index += 1
    print(f'{opora_index} опора = {math.sqrt(opora_count * (2 * R - opora_count))} м')  # висота
