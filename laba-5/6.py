file = open('./1.txt')

file.read(4)

print(file.readlines())

print(file.tell())

file.seek(0, 0)

print(file.readlines())
