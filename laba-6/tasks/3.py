import turtle

schedule = turtle.Turtle()
schedule.speed(0)

schedule.pensize(3)
schedule.screen.setup(800, 600)

def f(x):
    return 19 * x**8

schedule.up()
schedule.goto(-400, 0)
schedule.down()
schedule.goto(400, 0)
schedule.up()
schedule.goto(0, -300)
schedule.down()
schedule.goto(0, 300)
schedule.up()

schedule.color('red')
schedule.pensize(5)
for i in range(-12, 14):
    x = i * 0.1
    schedule.goto(x * 100  , f(x))
    schedule.down()
    schedule.dot(5)
  

schedule.screen.exitonclick()
