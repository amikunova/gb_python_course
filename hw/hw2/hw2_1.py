# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом.
# Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, чтобы
# все монетки лежали одной и той же стороной вверх. Входные данные:
# На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх,
# и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.

coins = [0, 1, 0, 1, 1, 0]
heads = coins.count(1)
tails = coins.count(0)
min_flips = min(heads, tails)

print(min_flips)

# count_zero = 0
# count_one = 0
#
# for coin in coins:
#     if coin == 0:
#         count_zero += 1
#     else:
#         count_one += 1
#
# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)
