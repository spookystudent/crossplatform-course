import turtle
square = turtle.Turtle()
square.up()
square.goto(-200,-200)
square.screen.setup(800, 800)
square.pensize(5)

square.down()

square.fd(400)
square.setheading(90)

square.fd(400)
square.setheading(180)
square.fd(400)

square.setheading(270)
square.fd(400)
square.setheading(45)
square.fd(200 * 1.41)

square.fd(200 * 1.41)

square.screen.exitonclick()
square.screen.mainloop()
