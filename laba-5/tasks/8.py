with open('./8.txt', 'r') as file:
   numbers = [int(line.strip()) for line in file]

print(f"Максимальное число: {max(numbers)}")
print(f"Минимальное число: {min(numbers)}")
