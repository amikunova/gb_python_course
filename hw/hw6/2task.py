def arithmetic_progression(a1, d, n):
    # Создаем список для хранения элементов арифметической прогрессии
    progression = []

    # Заполняем список элементами арифметической прогрессии
    for i in range(n):
        an = a1 + i * d
        progression.append(an)
    return progression


# Пример использования:
a1 = 1  # Первый элемент
d = 2  # Разность
n = 10  # Количество элементов

result = arithmetic_progression(a1, d, n)
for i in result:
    print(i)
