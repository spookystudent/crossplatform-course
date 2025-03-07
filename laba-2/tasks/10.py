import math

def power(x, y):
  return x ** y

def square_root(x):
  return math.sqrt(x)

def sin(x):
  return math.sin(x)

def cos(x):
  return math.cos(x)

def tan(x):
  return math.tan(x)

def calculate():
  print("Выберите операцию:")
  print("1. Возведение в степень")
  print("2. Квадратный корень")
  print("3. Синус")
  print("4. Косинус")
  print("5. Тангенс")

  choice = input("Введите номер операции (1/2/3/4/5): ")

  if choice == '1':
      num1 = float(input("Введите первое число: "))
      num2 = float(input("Введите второе число: "))
      print(f"Результат: {power(num1, num2)}")
  elif choice == '2':
      num = float(input("Введите число: "))
      print(f"Результат: {square_root(num)}")
  elif choice == '3':
      num = float(input("Введите число: "))
      print(f"Результат: {sin(num)}")
  elif choice == '4':
      num = float(input("Введите число: "))
      print(f"Результат: {cos(num)}")
  elif choice == '5':
      num = float(input("Введите число: "))
      print(f"Результат: {tan(num)}")
  else:
      print("Ошибка ввода")

calculate()
