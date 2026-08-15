"""
Кортежи (tuple)
Упорядоченный набор неизменяемых объектов
"""
#import copy
from string import ascii_lowercase, ascii_uppercase, digits, ascii_letters

print(ascii_letters)

tp = (22, 33, 44)
print(tp[1])
print(tp[:-1])
print(tp[::-1])
print(tp)
print(type(tp))

print(list(tp))
string = 'qwerty'
lst = list(string)
print(lst)

print(''.join(lst))

n = 7
print(type(n))
print(n)

tps = tuple(string)
print(tps)
print(''.join(tps))

t = 22

print(id(tp[0]), id(t))

print(ord('А')) #cyr
print(ord('A')) #lat
print(ord('\n'))
print(ord('\t'))
print(ord('\r'))

print(ord('2'))

print(chr(1049))

n, m, z = 7, 5, 8 #n = 7 # n = [7] # n = (7) получается кортеж
print(type(n))
print(n, m, z)

PI = 3.1415926,
print(PI)
print(type(PI))

name, *marks, last = 'Ivan', 4, 5, 3, 5, 7 # * - упаковывает в список
print(name)
print(marks)
print(*marks)
print(last)

tp = ('login', 'password')
print(tp)
print(id(tp))
buf = list(tp)
print(buf)

buf[-1] = 'qwerty'
print(buf)

tp = tuple(buf)
print(id(tp))

tp = (22, 33, 44, 22)
print(tp)

print(len(tp))
print(tp.count(22))
print(tp.index(22))
print(tp[0] == tp[-1])
print(tp[0] is tp[-1])
print(id(tp[0]), id(tp[-1]))

