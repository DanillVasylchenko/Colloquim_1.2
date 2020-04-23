"""
З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
що протягом цього часу температура знижувалася. Визначте, о котрій годині було
вперше зафіксовано від'ємну температуру.
Васильченко Даниїл Назарович 122А
"""
from random import randint

# -272 найнижча можлива температура та +142000000000000000000000000000000 - температура під час Великого Вибуху
start_temp = randint(-272, 142000000000000000000000000000000)
flag = False
# проходимо по годинам
for i in range(8, 21):
    # перевірка на мінусову температуру
    if start_temp < 0:
        print(f"О {i} годині температура стане від'ємною")
        flag = True
        break
    # нерівномірний спад температури(уявимо що можливмй анти Великий Вибух)
    start_temp -= randint(1, 142000000000000000000000000000000)

    # мінімальна можлива температура -272
    if start_temp < -272:
        start_temp = -272
# можливий варіант, що температура так і не зайде за 0
if not flag:
    print("Температура так і не стала мінусовою за чей час")