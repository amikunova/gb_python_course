#Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно,
# что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и
# он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему! Пользователь вводит одно число N —
# количество арбузов. Вторая строка содержит N чисел, записанных на новои строчке кажлое. здесь кажлое число -
# это масса соответствующего арбуза. Все числа натуральные и не превышают 3000

n_w = int(input('Введите колличество арбузов '))
min_weight = -1
max_weight = 3001

for i in range(n_w):
    x = int(input())
    if x < min_weight:
        min_weight = x
    if x > max_weight:
        max_weight = x

print(min_weight, max_weight)