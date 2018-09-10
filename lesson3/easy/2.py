# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def num_f(a,b,c):
    if a > b and a > c:
        print(a)
    if b > a and b > c:
        print(b)
    if c > a and c > b:
        print(c)

num_f(13,14,15)