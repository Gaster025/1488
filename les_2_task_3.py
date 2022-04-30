# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
# https://yapx.ru/v/R0WEK

def program(a):
    res = ''.join(reversed(a))
    return res

n = program(input())
print(n)
