import numpy

A = (
    (1, 1, -1),
    (2, -4, 1),
    (4, -3, 1),
)

B = (
    (1, 0, -4),
    (2, 5, -3),
    (4, -3, 2),
)

C = (
    (1, 2, 1),
    (1, -2, 4),
    (3, -5, 3),
)

# 1. D = A * (B - C)
D = numpy.array(A) @ (numpy.array(B) - numpy.array(C))
for i in range(len(D)):
    for j in range(len(D[i])):
        print(D[i][j], end='\t')

    print()
print()


# 2. Обратная матрица D
D_inv = numpy.linalg.inv(D)
for i in range(len(D_inv)):
    for j in range(len(D_inv[i])):
        print(f'{D_inv[i][j]:.2f}', end='\t')

    print()
print()

# 3. Определитель матрицы D
det_D = numpy.linalg.det(D)
print('Определитель', det_D, '\n')


# 4. Вывести только диагональные элементы матрицы D
for i in range(len(D)):
    for j in range(len(D[i])):
        if i == j or j + i == 2:
            print(D[i][j], end='\t')
        else:
            print(end='\t')

    print()
