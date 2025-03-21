# Найти старшего и младшего ребенка, записать в новый файл и старый переименовать в "Детский сад"
import os


os.rename('./Детский сад.txt', './3.txt')

data = {}
with open('./3.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip().split() for line in file.readlines()]

    for line in lines:
        name = ' '.join(line[:-2])
        age = int(line[-2])
        if name in data:
            data[name] = max(age, data[name])
        else:
            data[name] = age

    smallest = min(data.items(), key=lambda item: item[1])
    oldest = max(data.items(), key=lambda item: item[1])

    with open('./output_3.txt', 'w', encoding='utf-8') as out:
        out.write(f'{" ".join(list(map(str, smallest)))}\n{" ".join(list(map(str, oldest)))}')

os.rename('./3.txt', './Детский сад.txt')

    