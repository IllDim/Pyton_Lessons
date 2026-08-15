"""Множества (set)"""
#набор неупорядоченных уникальных значений (неизменяемых объектов)

# ls = [22, 33, 44, 44]
# st = set()
# st = set(ls)
# #st = {22, 33, 44, 44}
# print(st)
# st.clear()
# print(st)
# st.add(54)
# st.update('load')
# st.update({'old', 32})
# print(st)
# n = st.pop()# delete element
# #st.remove('old')
# st.discard(100)# if element exists
#
# print(st)
# print(n)

# try:
#     st.remove('old1')
#     n = int(input('input value: '))
#     if n == 100:
#         raise TypeError('Ошибка типа данных')
# except ValueError as err:
#     print(err)
# except KeyError as err:
#     print('Ошибка по ключу', err)
# except Exception as err:
#     print(err)
# else:
#     print('Ok')
# finally:
#     print('Always')

st1 = {1, 2, 33}
st2 ={1, 2, 44}

#res = st1.union(st2) объединение множеств
res = st1 | st2

res = st1.intersection(st2)# пересечение множеств
res = st1 & st2

res = st1.difference(st2)#вычитание множеств
res = st1 - st2

res = st1.symmetric_difference(st2)#симметрическая разница
res = st1 ^ st2

print(res)

st1 = {1, 2, 33} #супермножество
st2 ={1, 2, 44}
st3 = {1, 2}#подмножество

print(st3.issubset(st1))#если подможество
print(st1.issuperset(st3))#если супермножество


