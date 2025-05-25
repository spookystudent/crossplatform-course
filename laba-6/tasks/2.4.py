import turtle
lines = turtle.Turtle()
lines.speed(0)

lines.pensize(3)
lines.up()
lines.goto(-230,-100)
lines.setheading(45)


for i in range(8):
    lines.down()
    lines.left(130)
    lines.fd(40)
    lines.left(150)
    lines.fd(70)
    lines.left(150)
    lines.fd(40)
    lines.up()
    lines.setheading(45)
    lines.fd(30)


lines.right(180)
lines.fd(30)
lines.right(180)
lines.down()

for i in range(8):
    lines.fd(50)
    lines.right(135)
    lines.fd(35.355)
    lines.left(135)

lines.up()
lines.left(135)
lines.fd(282.84)
lines.setheading(90)
lines.down()

for i in range(8):
    lines.fd(30)
    lines.left(135)
    lines.fd(21.213)
    lines.setheading(90)


lines.screen.exitonclick()
lines.screen.mainloop()
