m = 1
with open('1.txt','r') as f:
    numbers = [int(line.strip()) for line in f.read().split(' ')]
    
    for num in numbers: m *= num

with open('output_1.txt','w') as f:
    f.write(str(m))
