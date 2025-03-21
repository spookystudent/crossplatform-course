file = open('./7.txt', 'w')

file.write('1234')

file.close()


file = open('./7.txt', 'r')
a = int(file.read())

print(a + 5)

file.close()