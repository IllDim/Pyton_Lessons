from datetime import datetime
import sys

# import random
#
# lst = ['камень', 'ножницы', 'бумага']
# dic = {'1': 'камень', '2': 'ножницы', '3': 'бумага'}


# while True:
#     s1 = random.choice(list(lst))
#     s2 = input('Выбери один из вариантов (камень, ножницы, бумага): ')
#
#     if s2 not in lst and s2 != 'выход':
#         print('Некорректный ввод данных. Повторите попытку')
#         continue
#
#     if s2 == 'выход':
#         print('Игра завершена.')
#         break
#     elif s1 == s2:
#         print('Ничья. Повторите попытку')
#         continue
#     elif (s1 == 'камень' and s2 == 'ножницы') or (s1 == 'ножницы' and s2 == 'бумага') or (s1 == 'бумага' and s2 == 'камень'):
#         print(f'Вы проиграли... =( ({s1}/{s2})')
#         continue
#     else:
#         print(f'Вы выиграли! =) ({s1}/{s2})')
#         continue

# winners = {'камень' : 'ножницы', 'ножницы' : 'бумага', 'бумага' : 'камень'}
# while True:
#     s1 = random.choice(list(lst))
#     s2 = input('Выбери один из вариантов (камень, ножницы, бумага): ')
#
#     if s2 not in lst and s2 != 'выход':
#         print('Некорректный ввод данных. Повторите попытку')
#         continue
#     elif s2 == 'выход':
#         print('Игра завершена.')
#         break
#     elif s1 == s2:
#         print('Ничья. Повторите попытку')
#         continue
#
#     for k, v in winners.items():
#         if k == s1 and v == s2:
#             print(f'Вы проиграли... =( ({s1}/{s2})')
#             break
#         else:
#             print(f'Вы выиграли! =) ({s1}/{s2})')
#             break
#

# today = datetime.date.today()
# dt = input('Введите дату своего рождения (dd.mm.yyyy): ')
# birth = datetime.strptime(dt, '%d-%m-%Y')
# now = datetime.now()
# print(now, birth)
# try:
#     b = datetime.strptime(input('Введите дату рождения (dd.mm.yyyy): '),'%d.%m.%Y')
# except ValueError:
#     print('Неверное значение даты')
#     sys.exit(1)
#
# n = datetime.now()
# age = 0
# word = ''
# if b <= n:
#     age = n.year - b.year
#     if n.month < b.month:
#         age -=1
#     if age % 10 == 1:
#         word = 'год'
#     elif age in [2,3,4,22,24,33,34,42,44,52,54,62,64,72,74,82,84,92,94,102,103,104]:
#         word = 'года'
#     else:
#         word = 'лет'
#     print(f'Вам {age} {word}')
# else:
#     print('Введенная дата превышает текущую =)')


# user = {'name': 'Anna', 'age': '20', 'city': 'Moscow'}
#
# print(f"Имя: {user.get('name')}, Возраст: {user.get('age')}")
#
# #user['city'] = 'Saint Petersburg'
# user.update({'city': 'Saint Petersburg'})
# print(f"Город: {user['city']}")
#
# #user['profession'] = 'Engineer'
# user.setdefault('profession', 'Engineer')
# print(f"Профессия: {user['profession']}")
#
# #del user['age']
# removed_age = user.pop('age', None)
# print(f"Удален возраст: {removed_age}")
#
# #has_email = 'email' in user.keys() #равнозначные записи
# has_email = 'email' in user#по умолчанию проверяет ключи
# print(f"Есть email: {has_email}")
#
# print("\nВсе ключи и значения:")
# for key, value in user.items():
#     print(f"{key}: {value}")

# text = "Осень в Москве, Зима в Москве, Весна в Москве, Лето в Москве. Времена года!"
# counts = {}
# st = text.lower().replace(',','').replace('.','').replace('!','').split()
#
# # for w in st:
# #     counts[w] = counts.get(w, 0) + 1
#
# for word in st:
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1
#
# # for w in ''.join(c if c.isalnum() or c.isspace() else ' ' for c in text).lower().split():
# #     counts[w] = counts.get(w, 0) + 1
# print(counts)

#разделить студентов по группам
# students = [
#     ('Anna', 'A'),
#     ('Ivan','B'),
#     ('Maria','A'),
#     ('Petr','B'),
#     ('Olga','C')
# ]
# print(students)
#
# grups = {}
#
# for name, group in students:
#     print(group)
#     if group not in grups:
#         grups[group] = []
#     grups[group].append(name)
# print(grups)

#Задача . Учёт товаров на складе
# Программа должна уметь:
# 1 — Показать товары
# 2 — Добавить товар
# 3 — Продать товар
# 4 — Пополнить остаток
# 5 — Изменить цену
# 6 — Общая стоимость склада
# 7 — Самый дорогой товар
# 8 — Товары с остатком меньше 3
# 0 — Выход

warehouse = {
    "laptop": {"price": 80000, "quantity": 5},
    "mouse": {"price": 1500, "quantity": 20},
    "keyboard": {"price": 4000, "quantity": 10}
}

while True:
    print(f'1 — Показать товары\n2 — Добавить товар\n3 — Продать товар\n4 — Пополнить остаток\n5 — Изменить цену\n6 — Общая стоимость склада\n7 — Самый дорогой товар\n8 — Товары с остатком меньше 3\n0 — Выход')

    choice = int(input('Выберите действие: '))
    if choice == 0:
        print('Выход')
        break
    elif choice == 1:
        for name, product in warehouse.items():
        #for name in warehouse:
            print(f'Товар: {name}, Цена {product['price']} руб., Остаток {product['quantity']} шт.')
    elif choice == 2:
        name = input('Введите наименование товара: ')
        price = int(input('Введите цену: '))
        quantity = int(input('Введите остаток: '))

        if name not in warehouse:
            warehouse[name] = {'price' : price, 'quantity' : quantity}
            print('Товар добавлен')
        else:
            print('Товар уже есть')
    elif choice == 3:
        name = input('Какой товар продать? ')
        quantity = int(input('Введите кол-во: '))

        if name not in warehouse:
            print(f'Товара {name} нет на складе')
        else:
            if warehouse[name]['quantity'] > quantity:
                warehouse[name]['quantity'] -= quantity
                print('Товар продан')
            else:
                print('Кол-во превышает допустимое')
    elif choice == 4:
        name = input('Какой товар пополнить? ')
        quantity = int(input('Введите кол-во: '))

        if name not in warehouse and quantity >0:
            print(f'Товара {name} нет на складе')
        else:
            if warehouse[name]['quantity'] > quantity:
                warehouse[name]['quantity'] += quantity
                print('Товар пополнен')
    elif choice == 5:
        name = input('У какого товара меняем цену? ')
        price = int(input('Новая цена: '))

        if name not in warehouse:
            print(f'Товара {name} нет на складе')
        else:
            if price > 0:
                warehouse[name]['price'] = price
            else:
                print('Цена не может быть нулевой')
    elif choice == 6:
        sm = 0
        for name, product in warehouse.items():
            sm += product['price'] * product['quantity']
        print(f'Общая стоимость товара {sm} руб')
    elif choice == 7:
        max_price = 0
        nm =''
        for name, product in warehouse.items():
            if product['price'] > max_price:
                max_price = product['price']
                nm = name
        print(f'У товара {nm} максимальная стоимость {max_price}')
    elif choice == 8:
        #cnt = 0
        lst = []
        for name, product in warehouse.items():
            if product['quantity'] < 3:
                lst.append(name)
        if len(lst > 0):
            print(f'Товары с остатком менее 3х: {' '.join(lst)}')
        else:
            print('Все товары в нужном кол-ве')

#pass заглушка для питона
            # for price, quantity in warehouse[name].items():
            #     print(name, price, quantity)
            #     if q > quantity:
            #         print('Кол-во превышает допустимое')
            #     else:
            #         quantity -= q
            #         warehouse[name] = {'price' : price, 'quantity' : quantity}
            #         print(warehouse[name])

