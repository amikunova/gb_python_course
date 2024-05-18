#В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми
# партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех
# классов. Выведите наименьшее число парт, которое нужно приобрести для них.

first_class = int(input('введите первое число: '))
second_class = int(input('введите второе число: '))
third_class = int(input('введите третье число: '))

total_students = first_class + second_class + third_class
desks_needed = total_students // 2 + total_students % 2

print(desks_needed)