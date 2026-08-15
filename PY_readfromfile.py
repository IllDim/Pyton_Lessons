# from idlelib.grep import findfiles
#
# findfiles('C:\Users\PC\Desktop\', 'log.txt')
#parts = ''
# from datetime import datetime
#
# c_inf = 0
# c_er = 0
# c_w = 0
# dates = []
#
# with open(r'C:\Users\PC\Desktop\log.txt', 'r', encoding = 'utf-8') as file:
#     print(file.name)
#     for line in file:
#         print(line.split()[1])
#         #parts = line.split()[1]
#         if line.split()[1] == 'INFO':
#             c_inf += 1
#         elif line.split()[1] == 'ERROR':
#             c_er += 1
#         elif line.split()[1] == 'WARNING':
#             c_w += 1
#         #min_d = (min(datetime(min_d)) for min_d in line.split()[0])
#         dates.append(line.split()[0])
# print(dates)
# #min_d = (min(datetime(min_d)) for min_d in dates)
# #max_d = (max(datetime(min_d)) for min_d in dates)
# pr = [datetime.strptime(d, '%Y-%m-%d') for d in dates]
# print(pr)
# min_d = min(pr).strftime('%Y-%m-%d')
# max_d = max(pr).strftime('%Y-%m-%d')
# Diff = (max(pr) - min(pr)).days
#
# print(f'Info: {c_inf}\nError: {c_er}\nWarning: {c_w}\n')
# print(f'Min: {min_d}, Max: {max_d}, Mean: {Diff}')

# def read_from_log(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             print(f"Файл: {filename}\n{'=' * 40}")
#             for line in file:
#                 print(line, end='')
#     except FileNotFoundError:
#         print(f"Файл '{filename}' не найден!")
#     except Exception as e:
#         print(f"Ошибка: {e}")
#
# read_from_log(r'C:\Users\PC\Desktop\log.txt')
#Astra Code

# Задача 9. Функция для работы со списком Напишите функцию process_list(lst), которая:
# Принимает список чисел.
# Возвращает новый список, где все чётные числа заменены на их квадраты, а нечётные — на их кубы.
# Обработайте случай, если на вход подан не список (выведите "Ошибка: аргумент не является списком").
# Переписать через списковое включение
# Переписать через lambda функцию.

def process_list(lst):
    # if not isinstance(lst, list):
    #     print('Ошибка. Объект не список.')
      #    return []

    # try:
    #     new_list = []
    #     for i in lst:
    #         if i % 2 == 0:
    #             new_list.append(i**2)
    #         else:
    #             new_list.append(i**3)
    #     return new_list
    # except Exception as ex:
    #     print(ex)

    new_list = [i**2 if i % 2 == 0 else i**3 for i in lst]
    return new_list

print(process_list([1,2,3,4,5,6,7,8,9]))


lst = [1,2,3,4,5,6,7,8,9]
new_list = list(map(lambda i: i**2 if i % 2 ==0 else i**3, lst))
print(new_list)

