with open('./7.txt', 'r') as file:
   numbers = [int(line.strip()) for line in file]

print(numbers)
product = 1
for num in numbers:
   product *= num
print(product)
