m = int(input('enter m'))
n = int(input('enter n'))

a = []

for i in range(m):
    b = []

    for j in range(n):
        print('Enter [',i,',',j,']')
        b.append(int(input()))
    a.append(b)

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()


for i in range(m):
    for j in range(n):
        if a[i][j] < 0:
            a[i][j] = 0
        elif a[i][j] > 0:
            a[i][j] = 1

for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()


