
# age = int(input('input age: '))
#
# if age >= 18:
#     print('access')
# else:
#     print('access denited')

# balance = 20000
# cash = int(input(('input cash: ')))
#
# if cash <= balance:
#     print('take your money')
#     balance -= cash
#     print(f'balance: {balance}')
# else:
#     print('no money in balance')

# x = int(input('input x: '))
# y = int(input('input y: '))
# op = input('input operation +,-,*,/: ')
# res = 0
# i = -1
# if op in ('+','-','*','/'):
#     match op:
#         case '+': res = x + y
#         case '-': res = x - y
#         case '*': res = x * y
#         case '/' if y != 0: res = x / y
#         case '/' if y == 0: print('Error', i := 0)
#
# if i != 0:
#     print(f'Result for operation \'{op}\' is: {res}')

#     if op == '+':
#         print(f'result = {x + y}')
#     else:
#         print(f'result = {x - y}')
# else:
#     print('incorrect symbols')

# login = 'login'
# password = 'password'
#
# while True:
#     log = input('input login: ')
#     pas = input('input password: ')
#     if login == log and password == pas:
#         print('Welcome')
#         break
#     else:
#         print('Access denied')

# users = ['user', 'user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7', 'user8', 'user9']
# passwords = ['passw', 'passw1', 'passw2', 'passw3', 'passw4', 'passw5', 'passw6', 'passw7', 'passw8', 'passw9']
#
# ul = users[0]
# i = 0
# for us in users:
#     #print(f'User {users[i]}')
#     #i += 1
#     count = 0
#     while True:
#         pas = input('input password: ')
#         if passwords[i] == pas:
#              print('Welcome')
#             break
#         else:
log = 'login'
cnt = 0
for i in range(10):
    logs = log
    while True:
        if cnt == 0:
            logs += str(i)
        #     log = input('input login: ')
        password = logs + 'pas'
        pas = input(f'input password for user "{logs}": ')
        if password == pas and cnt < 3:
            print('Welcome')
            cnt = 0
            break
        else:
            print(f'Access denied for user "{logs}"')
            cnt += 1
            if cnt == 3:
                print('Next user')
                cnt = 0
                break

