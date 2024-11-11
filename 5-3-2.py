# Использование списковых включений (list comprehension)
def count(numbers):
    negatives = [x for x in numbers if x < 0]
    positives = [x for x in numbers if x > 0]
    return (len(negatives), len(positives))

# Тестирование
numbers = [4, -8, 6, -9, -7, -6]
result = count(numbers)
print("Result:", result)