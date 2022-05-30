# Вариант 6
# Найдите сумму номеров минимального и максимального элементов.


from random import randrange

a = [randrange(1, 100) for i in range(int(input("Введите количество элементов списка: ")))]
setFromLost = set(a)
listFromSet = list(setFromLost)
print("Ваш список: \n" + str(setFromLost))
copyOfList = list.copy(listFromSet)
copyOfList.sort()
print("Ваш отсортированный список: \n" + str(copyOfList))
minNumber = copyOfList[0]
maxNumber = copyOfList[-1]
minIndex = listFromSet.index(minNumber)
maxIndex = listFromSet.index(maxNumber)
print("Минимальное число : " + str(minNumber) + ", а его позиция " + str(minIndex) + "\n")
print("Максимальное число : " + str(maxNumber) + ", а его позиция " + str(maxIndex) + "\n")
print("Следовательно сумма их номеров : " + str(minIndex +  maxIndex) + "\n")
