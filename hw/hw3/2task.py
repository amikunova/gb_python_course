# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

list_1 = [1, 2, 3, 4, 5]
k = 6
closest_element = min(list_1, key=lambda x: abs(x - k))
print(closest_element)