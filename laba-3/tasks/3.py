phone_number = input("Введите номер телефона: ")


if '+7' in phone_number and ''.join(list(map(
    lambda char: char if not char.isdigit() else "x",
    phone_number
))) == '+x(xxx)xxx-xx-xx':
    print("ДА")
else:
    print("НЕТ")
