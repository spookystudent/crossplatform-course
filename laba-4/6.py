A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
]

print('Massive A:')

# Вывод при помощи цикла
for i in A: print(' '.join(list(map(str, i))))

# Пример 1. Подсчет суммы элементов матрицы
s = 0
for i in A:
    for j in range(len(A[i])):
        s += A[i][j]

print('Sum = ', s)

S = 0
for row in A:
    for column in row:
        S += column

print('Sum = ', S)