s = "У лукоморья 123 дуб зеленый"

if 'я' in s:
   print(f"Буква 'я' встречается в строке. Позиция: {s.index('я')}")

print(f"Буква 'у' встречается в строке {s.count('у')} раз(а)")

if not s.isalpha():
   print(s.upper())

if len(s) > 4:
   print(s.lower())

s = 'О' + s[1:]

print(s)
