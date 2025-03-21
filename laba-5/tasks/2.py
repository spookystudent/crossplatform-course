with open('./1.txt', 'r') as f:
    numbers = [int(line) for line in f.read().split(' ')]

    with open('./output_2.txt', 'w') as new_f:
        new_f.write(f'Max: {max(numbers)}, Min: {min(numbers)}')