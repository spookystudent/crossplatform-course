n = 3

A = []

for i in range(n):
    A.append([9]*n)

for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()


maximum = A[0][2]
for i in range(n):
    for j in range(n):
        if maximum < A[i][j]:
            maximum = A[i][j]

print(maximum)