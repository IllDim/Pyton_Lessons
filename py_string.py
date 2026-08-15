"""Строки начальный курс."""

#s = 'Здравствуйте, \'гости!\''
s = 'ЗдраВствуйте, гости!'
# print(s)
# for i in s:
#     print(i, end='  ')
#     #pass #остановка
# print()
# print(len(s))
#
# #101 = 1 * 2**2 + 2**0
# #           4   +  1   = 5
#
# print(s[4])
# print(__doc__)

# for i in range(len(s)):
#     print(i, s[i], end='   ')
# print()
# print(len(s))

# print(s[:12]) #substring срезы
# print(s[4:])
# print(s[4::-1])
# print(s[::-1])

s1 = 'казак'
# print(s1[:])
# print(s1[::-1])
#
# if s1 == s1[::-1]:
#     print('Yes')
# else:
#     print('No')
#
# print(s[4:10:1])

print(s.isalpha())
print(s1.isalpha()) #из букв

s2 = '123456a'
s3 = ' '
print(s2.isdigit())# из цифр
print(s2.isalnum()) # цифры и буквы
print(s3.isspace()) # пробел

print(s.isupper()) #верхний регистр
print(s.islower()) #нижний регистр
print(s.lower())

print(s.startswith('Здрав'))# начинается ли
print('дра' in s)# входит ли подстрока
print(s.endswith('!'))

print(s.upper()) #первод в верхний регистр
#s = '\033[32mЗдравствуйте, гости!\033[0m' # символ подчеркивания и очистка форматирования
print(s.title()) #каждое слово с большой буквы

print(s.capitalize())# начало с большой буквы

print(s.center(40))# выравнивание по центру
print(s.rjust(40))#выравнивание по правому краю
print(s.ljust(40))#выравнивание по левому краю

print(s.swapcase())# меняет регистр букв
print(s.strip())# обрезает пробелы

print(s.strip('! З'))# обрезает по краям определенные символы
print(s.rstrip())#убирает справа
print(s.lstrip())#убирает слева

print(s.index('т'))#индекс символа в строке
print(s.index('т', 7))#индекс символа в строке начиная от
print(s.index('т', 7, 11))#индекс символа в диапазоне

print(s.find('т', 7, 11))
print(s.find('т', 11, 20))#индекс символа в диапазоне

print(s.replace('т', 'N'))
print(s.replace('т', 'N', 2))#кол-во замен символа

print(s.replace('т','N').replace('N', 'т'))#каскадные методы

s = 'ЗраВствуйте, гости!'
s = s.strip()
ls = s.split()#разбиение строку на список по разделителю
print(ls)

print(', '.join(ls))#склеивает список в строку

s1 = 'aaa bbb ccc ddd '
s2 = '111 222 333 444 '
# aaa 111 bbb 222 ccc 333 ddd 444

res = s1[:4] + s2[:4] + s1[4:8] + s2[4:8] + s1[8:12] + s2[8:12] + s1[12:16] + s2[12:16]
print(res)

res = ''
for i in range(0, len(s1), 4):
    res += s1[i:i + 4] + s2[i:i + 4]
print(res)

#s = '-3x^2+4x-6=0'
#a = -3, b = 4, c = -6

s = '-3x^2+4x-6=0'
#s = '12x^2+6x=0'
eq = s.replace(' ', '').replace('=0', '').replace('x^2', '').replace('x', '')

a = ''
b = ''
c = '0'

if eq[0] == '-':
    a = '-'
eq = eq.lstrip('-').replace('+',' +').replace('-', ' -').split()

a += eq[0]
b = str(eq[1]).replace('+','')
if len(eq) > 2:
    c = str(eq[2]).replace('+','')

if c == '0':
    print('a = ' + a + ',', 'b = ' + b)
else:
    print('a = ' + a + ',', 'b = ' + b + ',', 'c = ' + c)



