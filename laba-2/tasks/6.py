if (ticket:=input("Введите номер билета: ")) and sum([int(i) for i in ticket[:len(ticket)//2]]) == sum([int(i) for i in ticket[(len(ticket)//2) * -1:]]):
   print("Билет счастливый!")
else:
   print("Билет несчастливый.")