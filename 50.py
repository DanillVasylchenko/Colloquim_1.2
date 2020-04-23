"""
У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів
виграшних квитків. Перевірте, чи є квиток з номером N виграшним.
Васильченко Даниїл Назарович 122А
"""
import random
tickets = list(range(100))
win_tickets = []
N = int(input("Введіть номер Вашего квитка: "))
for i in range(10):
    a = random.choice(tickets)
    win_tickets.append(a)
    tickets.remove(a) # для виключення повторів
print(win_tickets)
if N in win_tickets:
    print("Ви виграли!")
else:
    print("Програш")