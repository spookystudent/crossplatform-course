x = int(input("Введите число от 1 до 9: "))

if 1 <= x <= 3:
   s = input("Введите строку: ")
   n = int(input("Введите число повторов строки: "))
   result = s * n
   print(result)
elif 4 <= x <= 6:
   m = int(input("Введите степень, в которую следует возвести число: "))
   result = x ** m
   print(result)
elif 7 <= x <= 9:
   for i in range(10):
       x += 1
       print(x)
else:
   print("Ошибка ввода")
