import string
from itertools import chain

N = 10  # Количество элементов в списках

# Генерация списка натуральных чисел
naturalNumbers = [i for i in range(1, N+1)]
print("Numbers:")
print(naturalNumbers)

# Генерация списка строк
stringsList = [letter for letter in string.ascii_lowercase[:N]]
print("String:")
print(stringsList)

# Функция для чередования элементов двух списков
def alternateLists(list1, list2):
    # Используем map и lambda для чередования
    combined = list(map(lambda x, y: [x, y], list1, list2))
    # Разворачиваем список списков в один список
    return list(chain.from_iterable(combined))

# Применение функции
finalList = alternateLists(naturalNumbers, stringsList)
print("Result:")
print(finalList)
