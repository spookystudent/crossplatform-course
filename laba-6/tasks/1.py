import turtle


t = turtle.Turtle()
t.speed(3)

t.down()

# Верхний полукруг
t.circle(25, 360)

# t.fd(40)
t.setheading(180)


t.circle(45, 360)
t.up()

t.goto(150, 100)


t.write('Голган Семён Сергеевич')

t.screen.exitonclick()
t.screen.mainloop()
