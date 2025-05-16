import turtle

a = (lambda : [  # noqa: E731
    t := turtle.Turtle(),
    t.screen.screensize(800, 800),

    rectangle := lambda w, h : [
        [
            t.left(90),
            t.fd(h),
            t.left(90),
            t.fd(w)
        ] for _ in range(2)
    ],

    rectangle(320, 200),
    t.screen.exitonclick(),
    t.screen.mainloop(),
])

a()