#Найдите сумму цифр трехзначного числа n. Результат сохраните в перменную res. n = 123

n = int(input('Введите число: '))
res = sum(int(digit) for digit in str(n))
print(res)

