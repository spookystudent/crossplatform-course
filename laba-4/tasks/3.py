"""
Матрица 3 на 3

Состоит из случайных цифр


Вторая, 1 на 3

Перемножить, посчитать определитель, найти обратную матрицу, перевести к диагональному виду, транспонировать

"""

import random


def print_matrix(matrix):
    for row in matrix:
        for column in row:
            print(column, end='\t')
        print()
    print()

A = [
    [random.randint(0, 100) for _ in range(3)] for _ in range(3)
]
B = [
    [random.randint(0, 100) for _ in range(1)] for _ in range(3)
]

print_matrix(A)

print_matrix(B)

# Перемножение
m = len(A)
n = len(B)
k = len(B[0])

C = [[None for __ in range(k)] for __ in range(m)]

for i in range(m):
    for j in range(k):       
        C[i][j] = sum(A[i][kk] * B[kk][j] for kk in range(n))
  
print_matrix(C)


# Найти определитель матрицы
def determinant(matrix):
    n = len(matrix)
    
    if n == 1: return matrix[0][0]
    if n == 2: return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    det = 0
    for col in range(n):
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]

        det += ((-1)**col) * matrix[0][col] * determinant(minor)
    
    return det


print(determinant(A))


# Обратная матрица
def inverse_2x2(matrix):
    det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    if det != 0:
        return [[matrix[1][1]/det, -matrix[0][1]/det],
                [-matrix[1][0]/det, matrix[0][0]/det]]
    
print_matrix(inverse_2x2(A))