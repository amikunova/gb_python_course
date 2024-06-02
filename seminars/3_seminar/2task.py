# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
#
# unique_numbers = len(set(list_1))
#
# print(unique_numbers)

#Дана последовательность из N целых чисел и числс К.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на
# К элементов вправо, К - положительное число.

list1 = [5, 4, 6, 7, -10]
k = int(input('Введите число: '))
k = k % len(list1)
list_res = []

for i in range(k):
    list_res.append(list1[len(list1) - 1 - i])
print(list_res)

for i in range(len(list1) - k):
    list_res.append(list1[i])
print(list_res)