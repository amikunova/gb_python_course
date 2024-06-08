# Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементами list_1 и границы диапазона в виде чисел min_
# number, max_number.


def find_indices_in_range(lst, min_number, max_number):
    indices = [i for i, value in enumerate(lst) if min_number <= value <= max_number]
    return indices

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

result = find_indices_in_range(list_1, min_number, max_number)
for index in result:
    print(index)


