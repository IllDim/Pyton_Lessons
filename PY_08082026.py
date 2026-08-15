#
# st = 'Иванов Иван Иванович, email:ivanov_ii@example.com, mel:+7(912)345-67-89, адрес:ул. Ленина, дом 15, кв 200'
#
# fio = st.split(',')[0]
#
# surname = pat = fio.split()[0]
# name = fio.split()[1][0]
# patr = fio.split()[2][0]
#
# print(fio)
# print(surname)
# print(name)
# print(patr)
#
# print(f'{surname} {name} {patr}')
#
# email = st.split(',')[1].replace('email:','').split('@')
# print(email[0].strip())
# print(email[1])
#
# print(st.split(',')[2].replace('mel:', '').strip())
# print(st.split(',')[3].replace('адрес:', '').strip(), ','.strip(), st.split(',')[4].strip(), ','.strip(), st.split(',')[5])
# adr = st.split(':')[3].strip()
# print(f'Пользователь: {surname} {name} {patr}\nemail: {email[0].strip()}\ndomen: {email[1]}\nадрес: {adr}')
#
from pip._internal.models import index

numbers = [12, 7, 18, 5, 9, 14, 21, 8, 30, 11, 4, 15]

#Выведите каждый второй элемент списка (начиная с первого).
# Выведите список в обратном порядке без использования метода reverse() (используйте срезы).
# Удалите из списка все элементы, которые делятся на 3 без остатка.

# print(numbers[::2])
# print(numbers[::-1])
# new_numbers = []
# for i in numbers:
#      if i % 3  != 0:
#          new_numbers.append(i)
# print(new_numbers)
#
# new_num = [i for i in numbers if i % 3 != 0]
# print(new_num)

# Исходный список:    ...
# Количество  элементов:    ...
# Четные числа:    ...
# Нечетные числа:    ...
# Максимальное  значение:    ...
# Минимальное  значение:    ...
# Среднее значение:    ...
# Отсортированный  список:    ...
# Список наоборот:

# print(numbers)
# print(len(numbers))
# new_num = [i for i in numbers if i % 2 == 0]
# print(new_num)
# print(max(numbers))
# print(min(numbers))
# average = round(sum(numbers) / len(numbers), 2)
# numbers.sort()
# print(numbers)
# print(sorted(numbers))
# print(numbers[::-1])

#Поиск и модификация кортежа Дан кортеж:
#fruits = ('яблоко', 'банан', 'груша', 'апельсин', 'банан', 'киви', 'банан', 'слива')
# Найдите индекс первого вхождения слова "банан".
# Посчитайте, сколько раз встречается слово "банан". С
# оздайте новый кортеж, в котором все элементы исходного кортежа
# повторяются дважды (например, ("яблоко", "яблоко", "банан", "банан", ...)).

# print(fruits.index('банан'))
# print(fruits.count('банан'))
# nf = ()
# cnt = 0
# st = ''
# for i in fruits:
#     nf += (i, i)
# print(nf)

#Задача 5. Операции с множествами Даны два множества: (
# set1 = {2, 4, 6, 8, 10, 12}
# set2 = {6, 8, 10, 14, 16, 18}
# 1. Найдите пересечение множеств.
# 2. Найдите объединение множеств.
# 3. Удалите из set1 все элементы, которые есть в set2 Проверьте, является ли set1 подмножеством set2.

# 1. Пересечение
# print(f"1. Пересечение: {set1 & set2}")
#
# # 2. Объединение
# print(f"2. Объединение: {set1 | set2}")
#
# # 3. Удаление элементов
# set1_copy = set1.copy()
# set1 -= set2  # или set1.difference_update(set2)
# print(f"3. set1 после удаления элементов из set2: {set1}")
#
# # 4. Проверка подмножества
# print(f"4. set1 ⊆ set2? {set1.issubset(set2)}")

#print(set1.isnumber(set2))

# dic = {'Иван': [5, 4, 5], 'Петр': [3, 4, 4], 'Мария': [5, 5, 4], 'Ольга': [4, 5, 5]}
# # Добавьте в словарь нового студента "Анна" с оценками [5, 5, 5]. Удалите студента "Петр".
# # Выведите средний балл для каждого студента (используйте цикл по ключам и значениям).
#
# dic['Анна']  = [5, 5, 5]
#
# print(dic)
#
# del dic['Петр']
# print(dic)
#
# for key,value in dic.items():
#     avetage = round(sum(value)/len(value), 2)
# print(avetage)

# import random
# con = random.randint(0, 100)
# count = 0
# while True:
#     key = int(input('Введите число: '))
#     count += 1
#     if key == con:
#         print('Угадал')
#         break
#     elif key > con:
#         print('Число больше')
#     elif key < con:
#         print('Число меньше')
#     else:
#         print('Мимо')
#         print(con)
# print(count)


# Напишите программу, которая принимает строку от пользователя и выводит:
# Количество гласных букв (а, е, ё, и, о, у, ы, э, ю, я).
# Количество согласных букв. Количество цифр. Самый часто встречающийся символ (исключая пробелы).
# from collections import Counter
# text = input('Введите строку: ')
# vowels = 'аеёиоуыэюя'
#
# print(f"Гласных: {sum(1 for c in text if c in vowels)}")
# print(f"Согласных: {sum(1 for c in text if c.isalpha() and c not in vowels)}")
# print(f"Цифр: {sum(c.isdigit() for c in text)}")
# print(f"Самый частый символ: {Counter(c for c in text if c != ' ').most_common(1)}")
#
#
# def analyze_string_simple(text):
#     """Упрощенная версия анализатора строки"""
#
#     # Гласные и согласные
#     vowels = set('аеёиоуыэюяАЕЁИОУЫЭЮЯ')
#     consonants = set('бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ')
#
#     # Счетчики
#     vowel_count = 0
#     consonant_count = 0
#     digit_count = 0
#     char_freq = {}
#
#     for char in text:
#         if char in vowels:
#             vowel_count += 1
#         elif char in consonants:
#             consonant_count += 1
#         elif char.isdigit():
#             digit_count += 1
#
#         if char != ' ':
#             char_freq[char] = char_freq.get(char, 0) + 1
#
#     # Самый частый символ
#     most_common = max(char_freq.items(), key=lambda x: x[1]) if char_freq else None
#
#     # Вывод
#     print(f"\nГласных: {vowel_count}")
#     print(f"Согласных: {consonant_count}")
#     print(f"Цифр: {digit_count}")
#     if most_common:
#         print(f"Самый частый символ: '{most_common[0]}' ({most_common[1]} раз)")
#     else:
#         print("Нет символов для анализа")
#
#
# # Использование
# text = input("Введите строку: ")
# analyze_string_simple(text)
# max_count = 0
# max_ch = ''
# count = 0
# for i in st:
#     count = st.count(i)
#     if count > max_count:
#         max_count = count
#         max_ch = i
# print(max_ch, max_count)

from turtle import *

def draw_landscape():

    penup()
    goto(-450, -350)
    pendown()
    color('green')
    begin_fill()
    for i in range(2):
        fd(1000)
        lt(90)
        fd(250)
        lt(90)
    end_fill()
    #exitonclick()

#draw_landscape()

def draw_sun():
    goto(250, 120)
    color('yellow')
    begin_fill()
    circle(100)
    end_fill()
    exitonclick()
#draw_sun()

def draw_sky():

    color('blue')
    penup()
    goto(-450, 0)
    begin_fill()
    for i in range(2):
        fd(1000)
        lt(90)
        fd(500)
        lt(90)
    end_fill()
    #exitonclick()

draw_landscape()
draw_sky()
draw_sun()





