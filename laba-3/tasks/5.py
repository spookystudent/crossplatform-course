string = input("Введите строку: ")
unique_digits = set()
for char in string:
    if char.isdigit() and string.count(char) == 1:
        unique_digits.add(char)
if unique_digits:
    print("".join(unique_digits))
else:
    print("НЕТ")
