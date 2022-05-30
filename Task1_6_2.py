# Вариант 6
# По целому n и n положительным целым числам определите, можно ли из них образовать подмножество, сумма элементов которого делится на n без остатка.
# Если можно, то найти любое из таких подмножеств.

import numpy
from random import randrange

n = (int(input("Введите целое число n: ")))

a = [randrange(1, 100) for i in range(n)]
print(a)
if a.__contains__(n):
    print("Подмножество как минимум равно: " + str(n))


def iterate(resourceList, iterateCounter):
    if iterateCounter != len(resourceList):
        result = []
        copyOfSource = resourceList.copy()
        result.append(copyOfSource.pop(iterateCounter))
        while len(copyOfSource) != 0:
            sum = 0
            for j in numpy.arange(0, len(result), 1):
                sum = sum + result[j]
            if sum % n == 0:
                print("Ответ: " + str(result))
                result.append(copyOfSource.pop())
            else:
                result.append(copyOfSource.pop())
        if len(resourceList) > iterateCounter:
            iterate(resourceList, iterateCounter + 1)


iterate(a, 0)
