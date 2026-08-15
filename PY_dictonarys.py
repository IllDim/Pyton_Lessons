"""Словари (dict)"""
#набор неупорядоченных пар ключ-значение, в котором ключи уникальны
d = {}
d = {'Pb':'свинец', 'Au': 'Золото'}

print(d['Pb'])
print(d.get('Pb1', 'нужный объект'))
print(d)
d['Pb'] = 'Свинец' #изменяем значение
d['Fe'] = 'Железо' #добавляем железо
n = d.setdefault('Pb', 22) #защищает от вставки по существующему ключу

d.update({3:33, 2:222})
key = 'Pb'
print(d[key])

n = d.pop(key)
nn = d.popitem()#удаляет последнюю добавленную пару

print(d, n, nn)
print(d.keys())
print(list(d.keys()))
print(list(d))
print(list(d.values()))
print(list(d.items()))

for k in d:
    print(k)
for v in d.values():
    print(v)
for k, v in d.items():
    print(k, v)

l = [22, 33, 44]
dd = dict.fromkeys(l, 'item')
print(dd)

dd = {i: i**2 for i in range(10, 20)}
print(dd)

ls = [('Pb1', 'свинец'), ('Au1', 'Золото')]
dd = dict(ls)
print(dd)
