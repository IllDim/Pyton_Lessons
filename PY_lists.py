import random

nums = [22, 33, 44, 55, 99]
# ls = [2, 3, 4, 5, 9, 10]
# print(nums)
#итерация по индексу
# for i in range(len(nums)):
#     #print(i)
#     print(i, nums[i], ls[i], end='  ')
# print()
#
# cnt = 0
# for i in nums:
#     print(cnt, i, end=' ')
#     cnt += 1
# print()
# print(list(enumerate(nums)))
# # for i in enumerate(nums): #формирует кортежи из списка
# #     #print(i, end=' ')
# #     print(i[0], i[1], end=' ')
# for i, j in enumerate(nums):
#     print(i, j, end=' ')
#
# print()
names = ['Fedor', 'Alice', 'Sasha', 'Glasha', 'Masha']
# names.sort()
# for n, name in enumerate(names, 1):
#     print(f'{n}. {name}')
#
# for i, j in zip(nums, ls): # объединяет два списка в кортеж
#     print(i)
#     print(i - j)

#генерация случайных вещественных чисел
print(random.random())
print(random.uniform(0.9, 1))
print(random.uniform(-100, -99))

#генерация целых чисел
print(random.randint(9, 10))
print(random.randrange(2, 100, 2))#четные
print(random.randrange(1, 100, 2))#нечетные

#случайный выбор из коллекции
print(random.choice(nums))
print(random.choice(range(2, 10, 3)))
print(random.choice(names))

#генерация коллекции случайных объектов
print(random.choices('abcdifgjkh', k = 4))
print(random.choices(names, k = 7))
print(random.sample(names, 3))#генерация уникальных значений max = len(names)

a = 'I like python, it is very useful for data analysis'
b = 'python is the best tools for dealing with big data'
#выписать вторую строку без слов в первой строке

# c = []
# a = a.replace(',', '')
# a = a.split()
# b = b.split()
# for word in b:
#     if word not in a:
#         c.append(word)
# res = [word for word in b if word not in a]
# print(' '.join(c))
# print(' '.join(res))
# print(' '.join([word for word in b if word not in a]))# лист компликатион
#
# res = random.sample(range(1000000), 1000000)
# for n, i in enumerate(res, 1):
#     print(n, i)
#     if i == 0:
#         break
#print([n for n in res if res == 0])

# def modify_last(tp_tuple, k):
#     pass
#
# mytuple1 = (1, 1, 2)
# mytuple2 = (2, 4)
# tpl_tuple = (mytuple1, mytuple2)
# mylist2 = modify_last()

s = 'hjsgd kjhsdf'
print(''.join([symb for n, symb in enumerate(s, 1) if n != 0]))

# count = int(input('Введите кол-во студентов: '))
# #data = []
# data = {}
# for i in range(count):
#     name, *marks = input('Введите строкой имя студента и его оценки через пробел: ').split()
#     # print(name)
#     # print(marks)
#     marks = [int(mark) for mark in marks]
#     print(marks)
#     mean = sum(marks) / len(marks)
#     #data.append([name, mean])
#     data[name] = round(mean, 2)
# print(data)

s = 'djsfhsldkhfjsdhjhfsjkdhsdkhfs'
print({symb: s.count(symb) for symb in set(s)})
res = {}
cnt = 0
#for symb in set(s):
for symb in s:
    res[symb] = s.count(symb)
    cnt += 1
print(res)
print(cnt)