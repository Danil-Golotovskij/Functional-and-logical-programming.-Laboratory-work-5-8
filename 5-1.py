n = 6  # Четное число

# Генерируем матрицу
matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]

print("Matrix:")
for row in matrix:
    print(row)

# Функция для суммирования средних элементов строки
sumMiddleElements = lambda row: row[n//2 - 1] + row[n//2]

# Применяем функцию к каждой строке матрицы
sum = list(map(sumMiddleElements, matrix))

print("\n Result:")
print(sum)
