import turtle
star = turtle.Turtle()
star.speed(0)

star.pensize(3)
star.left(180)

for i in range(4):
    x_1, y_1 = star.pos()
    star.left(45)
    star.fd(150)
    x_2, y_2 = star.pos()
    star.left(180)
    star.fd(150)
    star.left(135)

    star.fd(50)
    star.goto(x_2, y_2)
    star.goto(x_1, y_1)
    star.left(90)
    star.fd(50)

    star.goto(x_2, y_2)
    star.goto(x_1, y_1)

star.screen.exitonclick()
star.screen.mainloop()
