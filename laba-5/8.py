file = open('./8.txt', 'w')

file.write('row 1\n')
file.write('row 2\n')

file.close()

list_1 = []

file = open('./8.txt', 'r')
for line in file:
    list_1.append(line.strip())
    print(list_1)