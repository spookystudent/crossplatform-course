"""
2.
Задана квадратная матрица. Получить транспонированную матрицу (перевернутую относительно главной диагонали) и вывести на экран.
"""

import random


n = int(input("Введите размерность матрицы: "))

A = [[random.randint(0, 100) for i in range(n)] for j in range(n)]


for row in A:
    for column in row:
        print(column, end='\t')
    print()

for row_index in range(n):
    for column_index in range(n):
        if row_index != column_index and row_index < column_index:
            A[row_index][column_index], A[column_index][row_index] = A[column_index][row_index], A[row_index][column_index]

print('Edited:')
for row in A:
    for column in row:
        print(column, end='\t')
    print()
            
