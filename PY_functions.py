"""подпрограмма ждет когда ее вызовут"""

# def proba():
#     print('proba')
#     return 'function'
#
# n = proba()
# print(n)

# def summator(x = 100, y = 50):
#     #sum = 0
#     return x + y
#
# x = int(input('input x: '))
# y = int(input('input y: '))
#
# s = summator(x, y)
# ss = summator(x) #позиционный аргумент
# sss = summator(y = 100) #ключевой аргумент
# print(s)
# print(ss)
# print(sss)

def many_args(*args, **kwargs): #разное кол-во аргументов
    print(args)
    print(kwargs)
    return sum(args)

print(many_args(2, 4, 3, 4, y = 20, x = 34))
print(many_args())
print(many_args(44, 66, c = 76))

#область видимости переменных
#параметры функции и определенные в ней переменные называются локальными
