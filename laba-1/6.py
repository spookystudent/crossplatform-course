y = int(input("Введите год "))
c = y // 100 + 1 if y % 100 != 0 else y // 100

if y % 4 != 0:
    print(f'Обычный, {c} век')
    
elif y % 100 == 0:
    if y % 400 == 0:
        print(f"Високосный, {c} век")
    else:
        print(f"Обычный, {c} век")
else:
    print(f"Високосный, {c} век")