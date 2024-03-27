import turtle


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
turtle.speed(0)
turtle.pensize(2)

rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

for i in range(100):
    turtle.color(rainbow_colors[i % len(rainbow_colors)])
    turtle.forward(i * 10)
    turtle.left(144)

turtle.hideturtle()

turtle.done()
