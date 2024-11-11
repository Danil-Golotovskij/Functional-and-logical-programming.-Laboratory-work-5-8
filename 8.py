from functools import reduce
import random

# Генерируем массив из 20 элементов, состоящий из чисел от 0 до 5
array = [random.randint(0, 5) for _ in range(20)]
print("Mas:")
print(array)

# Преобразуем массив в последовательность булевых значений: 1, если элемент равен 0, иначе 0
flags = list(map(lambda x: 1 if x == 0 else 0, array))

# Функция-редуктор для нахождения максимальной последовательности нулей
def reducer(acc, elem):
    index, flag = elem
    if flag == 1:
        if acc['current_length'] == 0:
            acc['current_start'] = index
        acc['current_length'] += 1
        if acc['current_length'] > acc['max_length']:
            acc['max_length'] = acc['current_length']
            acc['max_start'] = acc['current_start']
    else:
        acc['current_length'] = 0
    return acc

# Инициализация аккумулятора
initial_acc = {'current_length': 0, 'current_start': 0, 'max_length': 0, 'max_start': 0}

# Применение reduce для нахождения максимальной последовательности
result = reduce(
    reducer,
    enumerate(flags),
    initial_acc
)

# Вывод результата
print(f"\n Lenght: {result['max_length']} and index: {result['max_start']}.")
