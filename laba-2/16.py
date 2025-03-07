def add(x, y):
    return x + y

print(add('123', '456'), add('abc', 'abc'))

def run():

    def get(value):
        return f'input() returns {value}'
    
    [print(get(input())) for i in range(3)]

run()