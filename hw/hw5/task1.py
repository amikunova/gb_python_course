def f(a, b):
    # Базовый случай: если b равно 0, то любое число в степени 0 равно 1
    if b == 0:
        return 1
    # Если степень отрицательная, то используем обратную степень
    elif b < 0:
        return 1 / f(a, -b)
    # Рекурсивный случай: умножаем a на результат функции для степени b-1
    else:
        return a * f(a, b - 1)

# Примеры использования:
print(f(2, 3))  # Должно вернуть 8
