Sum = 0

while True:
    a = int(input())
    if a == 5:
        break
    elif a < 0:
        continue

    Sum+= a
print(Sum)