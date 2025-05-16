import turtle
import math

t = turtle.Turtle()
t.screen.screensize(800, 800)
t.speed(0)

Oa = 100
OA = 200

OC = (OA * 2) / (2 ** 0.5)

for i in range(1000):
    t.left(45)
    t.fd(OC)
    t.left(180)
    alpha = (math.asin(Oa / OC) * 180) / math.pi
    t.right(alpha)
    t.fd(
        ((Oa ** 2 + OA ** 2) ** 0.5) * 0.99
    )

    t.left(90 - alpha - 3.5)
    t.fd(Oa*1.1)

    t.left(22.5)


t.screen.exitonclick()
t.screen.mainloop()