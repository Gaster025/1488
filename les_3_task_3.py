# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list2 = []
x = 0
while len(my_list) != len(my_list2):
    x = x + 1
    my_list2.append(my_list[-0 - x])

print(my_list2)
