import random

result = None
for _ in range(10):
    num = random.randint(1, 100)
    if num % 2 == 0 and num % 3 != 0:
        if result is None or num < result:
            result = num
print(result)
