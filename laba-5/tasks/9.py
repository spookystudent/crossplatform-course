import math

x = [round(-1 + i * 0.1, 1) for i in range(21)]

y1 = [
    (1 + abs(xi)) ** 0.5
    for xi in x
]

y2 = [
    (1 + xi) / (2 + math.cos(xi) ** 2)
    for xi in x
]

y = [y1i * y2i for y1i, y2i in zip(y1, y2)]
y.sort()
max_y = max(y)

print(f"Произведение y1 и y2: {y}")
print(f"Максимальное значение y: {max_y}")

with open('data.txt', 'w', encoding='utf-8') as file:
   file.write(f"Произведение y1 и y2: {y}\nМаксимальное значение y: {max_y}")
       
