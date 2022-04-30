# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,
# … Количество элементов (n) вводится с клавиатуры.
# https://yapx.ru/v/R0WEu

def fun(h, sign=-1):
    k = h - 1
    sign = -sign
    if h == 0:
        return ''
    return fun(k, sign) + ' ' + str(sign / (1 << k))


n = int(input())
print(fun(n))
print(sum(map(float, fun(n).split())))
