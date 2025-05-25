import turtle

n = int(input('Введите n: '))

screen = turtle.Screen()

btn = turtle.Turtle()
btn.hideturtle()
btn.penup()
btn.goto(-20, -20)
btn.pendown()
btn.circle(40)
btn.penup()
btn.goto(-18, 16)
btn.write('btn', align='center', font=('Arial', 12, 'normal'))
btn.goto(-17, 0)

def draw_star(x, y):
    if -100 < x < 100 and -100 < y < 100:
        btn.clear()
        figure = turtle.Turtle()
        figure.pensize(3)
        for i in range(n):
            figure.fd(70)
            figure.left(180 - (180 * (n - 2)) / n)

btn.screen.onclick(draw_star)
turtle.listen()
turtle.mainloop()
