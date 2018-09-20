# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры,
#  точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

import re

pattern_name = '^[А-Я][а-я]+ [А-Я][а-я]+'
pattern_email = '^([a-z0-9_]+)@[a-z0-9]+\.(ru|org|com)$'

name = input('Введите имя и фамилию заглавными буквами ')

while True:
    search_name = re.search(pattern_name, name)
    if not search_name:
        name = input('Введите имя и фамилию заглавными буквами ')
    else:
        break

email = input('Введите корректный email (допускаются только домены домены .ru, .org, .com)')

while True:
    search_email = re.search(pattern_email, email)
    if not search_email:
        email = input('Введите корректный email (допускаются только домены домены .ru, .org, .com)')
    else:
        break

print(name, email)
