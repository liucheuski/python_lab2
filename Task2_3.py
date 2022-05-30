# Даны две квадратных таблицы чисел. Требуется построить третью, каждый элемент которой равен сумме элементов,
# стоящих на том же месте в 1-й и 2-й таблицах.

from random import randrange

n = (int(input("Введите целое число n: ")))

a = [[randrange(1, 100) for i in range(n)]] * n
print(a)
b = [[randrange(1, 100) for i in range(n)]] * n
print(b)

result = [[a[i][j] + b[i][j] for j in range
(len(a[0]))] for i in range(len(a))]

for r in result:
    print(r)
