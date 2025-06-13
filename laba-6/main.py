import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(2)
t.color("green")
t.pensize(10)
t.hideturtle()




button_mask = turtle.Turtle()
button_mask.penup()
button_mask.goto(0, 0)

button_mask.begin_poly()
button_mask.fd(100)
button_mask.right(60)
button_mask.fd(50)
button_mask.right(120)
button_mask.fd(150)
button_mask.right(120)
button_mask.fd(50)
button_mask.right(60)
button_mask.end_poly()
button_mask.clear()
button_mask.hideturtle()

poly = button_mask.get_poly()
screen.register_shape("trapezoid", poly)

button = turtle.Turtle()
button.left(90)
button.shape("trapezoid")
button.fillcolor("red")
button.penup()



def listok(t: 'turtle.Turtle'):
    t.down()
    t.fd(100)
    t.circle(50, 180)
    t.circle(75, 90)
    t.left(90)
    t.circle(75, 90)
    t.circle(50, 180)
    t.fd(100)
    t.up()

def stebel(t: 'turtle.Turtle'):
    t.backward(20)
    t.right(90)

    t.down()
    t.fd(200)
    t.circle(10, 180)
    t.fd(200)
    t.up()

is_drawing = True
def draw(x, y):
    if not is_drawing: return

    button.clear()
    button.hideturtle()
    t.showturtle()
    [(listok(t), t.fd(20)) for _ in range(4)]
    stebel(t)

button.onclick(draw)

t.hideturtle()
turtle.done()