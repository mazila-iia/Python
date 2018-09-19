# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

import os
import shutil


def changedir(file):
    curdir = os.getcwd()
    fullpath = os.path.join(curdir, file)
    if file == '../':
        os.chdir(file)
        fullpath = os.getcwd()
        print('Вы в директории {}\n'.format(fullpath))
    else:
        try:
            os.chdir(fullpath)
            print('Вы в директории {}\n'.format(fullpath))
        except FileNotFoundError:
            print('Директории не существует!\n')


def listdir():
    return os.listdir()

def deldir(file):
    curdir = os.getcwd()
    fullpath = os.path.join(curdir, file)
    try:
        os.rmdir(fullpath)
        print('Директория удалена! \n')
    except FileNotFoundError:
        print('Директории не существует!\n')
    except NotADirectoryError:
        print('Это файл, а не директория! \n')


def makedir(file):
    curdir = os.getcwd()
    fullpath = os.path.join(curdir, file)
    try:
        os.mkdir(fullpath)
        print('Директория создана! \n')
    except FileExistsError:
        print('Невозможно создать файл, так как он уже существует! \n')

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

numdir = [i for i in range(1, 10)]
for i in numdir:
    makedir('dir_' + str(i))

pattern = 'dir_'
for file in os.listdir():
    if pattern in file:
        deldir(file)

# Напишите скрипт, отображающий папки текущей директории.


listdir = os.listdir()
for i in listdir():
    curdir = os.getcwd()
    # т.к. в условии сказано, что только папки, я делаю проверку (пытаюсь зайти в директорию и выхожу из нее)
    try:
        os.chdir(curdir + '/' + i)
        os.chdir('../')
    except NotADirectoryError:
        continue
    print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


shutil.copyfile(__file__, __file__ + '.bac')