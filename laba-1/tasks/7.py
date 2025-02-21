money = int(input())

banknotes = []
banknotes_data = [500, 100, 10, 2]

for banknote in banknotes_data:
    while True:
        if money >= banknote:
            banknotes.append(banknote)
            money -= banknote
        else: break
else:
    if money != 0: print("NO!!!!")
    else:
        for banknote in [500, 100, 10, 2]:
            print(banknote, banknotes.count(banknote))
        print(f'Total: {sum(banknotes)}')
