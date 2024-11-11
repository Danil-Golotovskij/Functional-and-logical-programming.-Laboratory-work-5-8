class Iterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
        self.memo = {}  # Для мемоизации вычисленных значений

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        result = self.F(self.current)
        self.current += 1
        return result

    def F(self, n):
        if n in self.memo:
            return self.memo[n]
        if n <= 3:
            result = n
        elif n % 3 == 0:
            result = n ** 3 + self.F(n - 1)
        elif n % 3 == 1:
            result = 4 + self.F(n - 3)
        else:
            result = n ** 2 + self.F(n - 2)
        self.memo[n] = result
        return result


def generator(start, end):
    memo = {}  # Для мемоизации вычисленных значений

    def F(n):
        if n in memo:
            return memo[n]
        if n <= 3:
            result = n
        elif n % 3 == 0:
            result = n ** 3 + F(n - 1)
        elif n % 3 == 1:
            result = 4 + F(n - 3)
        else:
            result = n ** 2 + F(n - 2)
        memo[n] = result
        return result

    for n in range(start, end + 1):
        yield F(n)

# Создаем итератор для n от 1 до 10
iterator = Iterator(1, 10)

print("Iterator:")
for value in iterator:
    print(value, end=' ')
print()

# Повторная попытка итерировать 
print("Retry:")
for value in iterator:
    print(value, end=' ')
print()

# Создаем генератор для n от 1 до 10
generator = generator(1, 10)

print("Generator:")
for value in generator:
    print(value, end=' ')
print()

# Повторная попытка итерировать 
print("Retry:")
for value in generator:
    print(value, end=' ')
