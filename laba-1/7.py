numbers = [int(input(f'Введите {i + 1} число ')) for i in range(3)]

for number in numbers:
    print(f'Число {number} {"четное" if number % 2 == 0 else "нечетное"}')

