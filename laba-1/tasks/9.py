Sc = int(input("Circle: "))
Ss = int(input("Square: "))

radius = (Sc // 3.14) ** 0.5
side = Ss ** 0.5

print("YES" if radius*2 < side else "NO")
print("YES" if radius*2 > side else "NO")