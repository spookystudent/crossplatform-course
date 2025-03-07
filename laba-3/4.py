Sum = 0

a = int (input ("Enter a number: "))

while a != 5:
    Sum += a
    if a < 0:
        print('отрицательное число')
        break

    a = int(input())

else:
    print('Все числа положительные')
    print(Sum)