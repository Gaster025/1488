# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://yapx.ru/v/R0WC5

x = input('Введите натуральные числа: ')

for i in x:
    x = int(i)
    if x % 2 == 0:
        print(f'чётные: {x}')
    else:
        print(f'Нечётные: {x}')
