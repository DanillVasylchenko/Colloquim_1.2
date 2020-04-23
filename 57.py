"""
Відомість на зарплату представлена як дві таблиці. Одна містить
прізвища працівників цеху, а друга - їх зарплату за поточний місяць. Знайдіть прізвище
працівника, зарплата якого найменш відхиляється від середньої зарплати всіх
працівників за поточний місяць. Знайдіть прізвища двох працівників з найбільшою
заробітною платою. Видаліть з відомості на зарплату відомості про працівника,
зарплата якого мінімальна.
Васильченко Даниїл Назарович 122А
"""
import numpy as np

length = int(input('Введіть кіклькість працівників: '))

workers = [input("Прізвище працівника: ") for i in range(length)]
workers_2 = workers[:] # для використання після видалень із основного масиву

payment = [int(input("Заробітня плата: ")) for i in range(length)]
payment_2 = payment[:]

average_payment = np.array(payment).mean()

print(min(payment,
          key=lambda num: abs(num - average_payment)))  # це функція, яка виражає поняття "наближене до середнього"
# - чим це значення менше тим ближче до середнього (при нулі збігається із середнім)
for i in range(2):
    max_pay = max(payment)
    max_worker = workers[payment.index(max_pay)] # знаходимо ідентичний індекс зарплатні у списку робітників
    print(f"Найбільша зарплата {max_pay}грн. у {max_worker}")
    workers.remove(max_worker)
    payment.remove(max_pay)

# працюємо із workers_2 та payment_2 оскільки видалялт елементи з початкових списків
print(f"Зі списку видалено невдаху {workers_2[payment_2.index(min(payment_2))]} із зарплатнею {min(payment_2)}грн.")
print("Список працівників та їх заробітніх плат:")
for i in range(len(payment_2)):
    print(f"{workers_2[i]} - {payment_2[i]}")