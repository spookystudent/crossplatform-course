menu = {
   "Борщ": 35,
   "Котлета": 40,
   "Каша": 20,
   "Чай": 3
}

sorted_menu = sorted(menu.items(), key=lambda x: x[1])

print("Отсортированный список блюд по возрастанию цены:")
for dish, price in sorted_menu:
   print(f"{dish}: {price}")
