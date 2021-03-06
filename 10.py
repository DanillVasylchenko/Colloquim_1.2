"""
Дані про температуру повітря за декаду листопада зберігаються в масиві.
Визначити, скільки разів температура опускалася нижче -10 градусів.
Васильченко Даниїл Назарович 122А
"""
import numpy as np
from random import randint

# Введення массиву(під час листопаду може статись Великий Вибух)
input_massive = np.array([randint(-272, 142000000000000000000000000000000) for i in range(10)])

# Виведення масиву та к-ті разів виходу за -10 градусів
print("Ваш масив: ", input_massive)
print("К-ть разів зниження температури за -10 градусів: ", sum(i < -10 for i in input_massive))