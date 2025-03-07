a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))


if a > b:
    print(f'{a} > {b}; {a} - {b} = {a - b}')
else:
    print(f'{b} > {a}; {b} - {a} = {b - a}')

c = int(input('Введите первое число c: '))
d = int(input('Введите первое число d: '))

if c < d:
    print(f'{c} < {d}; {c} - {d} = {c - d}')
else:
    print(f'{c} > {d}; {d} - {c} = {d - c}')


e = int(input('Введите первое число e: '))
f = int(input('Введите первое число f: '))

if e < f:
    print(f'{e} < {f}; {e} - {f} = {e - f}')
else:
    print(f'{e} > {f}; {f} - {e} = {f - e}')


i = 0
while i < 3:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))

    if a > b:
        print(f'{a} > {b}; {a} - {b} = {a - b}')
    else:
        print(f'{b} > {a}; {b} - {a} = {b - a}')

        i += 1

def diff():
    m = int(input('Введите первое число: '))
    n = int(input('Введите второе число: '))

    if m > n:
        print(f'{m} > {n}; {m} - {n} = {m - n}')
    else:
        print(f'{m} < {n}; {n} - {m} = {n - m}')
    
    return m, n

a, b = diff()
c, d = diff()
e, f = diff()