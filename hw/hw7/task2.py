def print_operation_table(operation, num_rows=9, num_columns=9):
    # Проверяем, что число строк и столбцов больше 2
    if num_rows < 2 or num_columns < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return

    # Генерируем и выводим таблицу
    for i in range(1, num_rows + 1):
        row = [str(operation(i, j)) for j in range(1, num_columns + 1)]
        print(" ".join(row))

# Пример использования:
print_operation_table(lambda x, y: x * y, 3, 3)
