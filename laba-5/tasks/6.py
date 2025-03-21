import random

with open('./6.txt', 'w') as file:
   for _ in range(10):
       file.write(str(random.randint(1, 100)) + '\n')
