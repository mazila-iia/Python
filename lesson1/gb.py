# https://www.python.org/
# https://www.jetbrains.com/pycharm/download/ # Community
# GIT - 9 урок.

number = 5  # int (integer)
name = 'Alex'  # str (string)
surname = "Ivanov"
some_number = '123123'
money = 10.30  # float дробное
is_admin = False
is_god = True

####
my_list = [1, 2, 3, 'qwe', 50.23, True]  # list (массив)
my_tuple = (1, 2, 3, 'qwe', 50.23, True)  # неизменяемый list список
my_dict = {'name': 'Alex', 'age': 20}
###

# print(number + 1)
# print(number - 1)
# print(number / 1)
# print(number * 1)
# print(number // 2)
# print(number % 2)
# print(number ** 2)

# Ctrl(CMD) + /

'''
qwerty
asdfgh
zxcvbn
'''

# name = 'Alex'
# name = 'Olga'
# NAME = 'Alex' # Соглашение между программистами, что значение менять нельзя.

# name = input('Введите имя:') # 'Alex' - str тип строка.
# print('привет', name)

# int()
# float()
# str()
# bool()

# age = float(input('Возраст:'))
# print(age + 10)
# print(age + 20)
# print(age + 30)

# print(1.111111 + 1.11111111)
# round()
# a = 5
# # b = 1
# #
# # print(5 > 1)
# # print(5 < 1)
# # print(5 == 1)
# # print(5 != 1)
# # print(5 >= 1)
# # print(5 <= 1)

# print(bool(0)) # boolean Булев тип
# print(bool(''))
# print(bool(1))
# print(bool(-1))
# print(bool('123'))

# PEP-8
# correct_password = 'qwerty'
# correct_password2 = 'qwerty2'
# correct_password3 = 'qwerty3'
# password = input('Password:')
#
# if password == correct_password:
#     print('Пароль верный!')
# elif password == correct_password2:
#     print('Второй пароль подошел!')
# elif password == correct_password3:
#     print('Третий пароль подошел!')
# else:
#     print('Пароль неверный!')


# Ctrl + D - дублирование строки
# Ctrl(CMD) + Alt + L - автоформатирование кода

i = 0
while i < 10:
    i += 1

    # if i == 5:
    #     break # Останавливает цикл
    # elif i == 3:
    #     continue # Пропускает данный шаг и переходит на следующий
    print(i)
    # i = i + 1
else:
    print('Сработает, если цикл завершился по условию!')

print('После цикла')
