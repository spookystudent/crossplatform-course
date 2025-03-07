import random


Sum = 0 

while True:
    # a = int(input())
    a = random.randint(0,10)

    if a == 5:
        break

    Sum += a

print(Sum)