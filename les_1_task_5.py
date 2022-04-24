# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

# ссылка на диаграмму https://yapx.ru/v/RyJdO

import string

a = input('Введите первую букву: ')
b = input('Введите первую букву: ')

z = string.ascii_lowercase.index(a)
v = string.ascii_lowercase.index(b)
print(f'Буква {a} будет номер {z} а буква {b} будет номер {v}')

g = v - z - 1
print(f'Между {a} и {b}, находится {g} буквы')