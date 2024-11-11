import sys
import time
from functools import lru_cache
from datetime import datetime

# Функция для замера производительности
def measurePerformance(func, *args):
    startTime = time.perf_counter()
    result = func(*args)
    endTime = time.perf_counter()
    elapsedTime = endTime - startTime
    memoryUsage = sys.getsizeof(result)
    return result, elapsedTime, memoryUsage


# Обычная рекурсивная функция
def Frecursive(n):
    if n <= 3:
        return n
    elif n % 3 == 0:
        return n * n * n + Frecursive(n - 1)
    elif n % 3 == 1:
        return 4 + Frecursive(n - 3)
    else:
        return n * n + Frecursive(n - 2)

# Функция с ручной мемоизацией
memo = {}
def Fmemoization(n):
    if n in memo:
        return memo[n]
    if n <= 3:
        result = n
    elif n % 3 == 0:
        result = n * n * n + Fmemoization(n - 1)
    elif n % 3 == 1:
        result = 4 + Fmemoization(n - 3)
    else:
        result = n * n + Fmemoization(n - 2)
    memo[n] = result
    return result

# Функция с использованием @lru_cache
@lru_cache(maxsize=None)
def FlruCache(n):
    if n <= 3:
        return n
    elif n % 3 == 0:
        return n * n * n + FlruCache(n - 1)
    elif n % 3 == 1:
        return 4 + FlruCache(n - 3)
    else:
        return n * n + FlruCache(n - 2)

n = 347

# Без мемоизации
result, elapsedTime, memoryUsage = measurePerformance(Frecursive, n)
print("Without memoization:")
print(f"Result: {result}")
print(f"Time: {elapsedTime:.6f} sec")
print(f"Memory usage: {memoryUsage} byte")

# С ручной мемоизацией
memo.clear()
resultMemo, elapsedTimeMemo, memoryUsageMemo = measurePerformance(Fmemoization, n)
print("\n With memoization:")
print(f"Result: {resultMemo}")
print(f"Time: {elapsedTimeMemo:.6f} sec")
print(f"Memory usage: {memoryUsageMemo + sys.getsizeof(memo)} byte")

# С использованием @lru_cache
FlruCache.cache_clear()
resultLru, elapsedTimeLru, memoryUsageLru = measurePerformance(FlruCache, n)
print("\n With @lru_cache:")
print(f"Result: {resultLru}")
print(f"Time: {elapsedTimeLru:.6f} sec")
print(f"Memory usage: {memoryUsageLru} byte")

