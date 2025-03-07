def get_user_age():
   return int(input("Введите ваш возраст: "))

def get_user_choice():
   return input("Выберите вариант: ")

print("Программа определения места работы")

while True:
    age = get_user_age()

    if 0 <= age <= 7:
        print("Вам в детский сад")
    elif 7 < age <= 18:
        print("Вам в школу")
    elif 18 < age <= 25:
        print("Вам в профессиональное учебное заведение")
    elif 25 < age <= 65:
        print("Вам на работу")
    elif 65 < age <= 120:
        print("Вам предоставляется выбор")
    else:
        print("Ошибка ввода")