a = [0, 1, 2, 3, 4, 10, 13, 21, 34, 55, 89, 100,16]

for element in a:
    if element < 35 and element % 2 == 0:
        print(element)
        
        
N = int(input("Количество элементов: "))

numbers = [int(input('Введите число: ')) for i in range(N)]

average = sum(numbers) / N
_max = max(numbers)
_min = min(numbers)

print(f'Ср. арифм.: {average}')
print(f'Макс: {_max}')
print(f'Мин: {_min}')