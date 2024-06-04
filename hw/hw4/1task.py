# Входные данные
n = 5
m = 6
set1_elements = "1 2 3 4 5"
set2_elements = "4 5 6 7 8 4"

# Преобразуем строки элементов в списки целых чисел
set1_list = list(map(int, set1_elements.split()))
set2_list = list(map(int, set2_elements.split()))

# Преобразуем списки в множества для удаления дубликатов
set1 = set(set1_list)
set2 = set(set2_list)

# Найдем пересечение множеств
common_elements = set1.intersection(set2)

# Преобразуем результат в отсортированный список
result = sorted(common_elements)

# Вывод результата
print(result)  # Вывод: [4, 5]
