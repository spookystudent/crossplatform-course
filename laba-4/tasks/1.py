"""
1.
Задана матрица порядка n и число к. Разделить элементы k-й строки на диагональный элемент, расположенный в этой строке.
"""
import random


n = int(input("Введите размерность матрицы: "))
k = int(input("Введите номер строки: "))

A = [[random.randint(0, 100) for i in range(n)] for j in range(n)]

for row in A:
    for column in row:
        print(column, end='\t')
    print(f'<-- k = {k}' if A.index(row) == k else '')

for row in A:
    if A.index(row) == k:
        print('*', end='\t')
    else:
        print(end='\t')
print()

for column in A[k][:k]:
    print(column, '\t', end='')

print()
for column in A[k][k:]:
    print(column, '\t', end='')