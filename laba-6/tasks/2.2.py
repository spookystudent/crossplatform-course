import turtle

cube = turtle.Turtle()
cube.speed(0)

cube.pensize(3)

for i in range(2):
    cube.right(90)

    cube.fd(120)
    cube.right(90)

    cube.fd(120)

cube.left(50)

cube.fd(62)
cube.left(130)

cube.fd(129)
cube.left(56)

cube.fd(58)

cube.up()
cube.goto(0, -120)
cube.down()
cube.left(170)
cube.fd(60)
cube.setheading(90)

cube.fd(125)
cube.screen.exitonclick()
cube.screen.mainloop()
