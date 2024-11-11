# Использование функций filter и lambda
def count(numbers):
    negatives = list(filter(lambda x: x < 0, numbers))
    positives = list(filter(lambda x: x > 0, numbers))
    return (len(negatives), len(positives))

# Тестирование
numbers = [4, -8, 6, -9, -7, 2]
result = count(numbers)
print("Result:", result)
