import turtle
lines = turtle.Turtle()
lines.speed(5)

lines.pensize(3)
lines.up()
lines.goto(-350, 0)
lines.setheading(45)
lines.down()
delta = 30
while delta != 100:
    lines.fd(delta)
    lines.right(90)
    lines.fd(delta)
    lines.right(90)
    lines.fd(delta)
    lines.right(90)
    lines.fd(delta)
    lines.right(180)
    lines.fd(delta)
    lines.left(90)
    lines.fd(delta)   
    delta += 10
    if delta > 40:
        lines.up()
        lines.left(135)
        lines.fd(delta / 2.5)
        lines.right(135)
        lines.down()

lines.screen.exitonclick()
lines.screen.mainloop()
