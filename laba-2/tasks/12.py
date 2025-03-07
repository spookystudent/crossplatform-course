import math

def calculate_perimeter(a, b, c):
   return a + b + c

def calculate_area(a, b, c):
   s = (a + b + c) / 2
   return math.sqrt(s * (s - a) * (s - b) * (s - c))

a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))

perimeter = calculate_perimeter(a, b, c)
area = calculate_area(a, b, c)

print(f"Периметр треугольника: {perimeter}")
print(f"Площадь треугольника: {area}")
