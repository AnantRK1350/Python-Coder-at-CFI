import turtle

screen = turtle.Screen()
screen.bgcolor("black")
turtle.speed(0)
turtle.pensize(2)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

for i in range(360):
    turtle.pencolor(colors[i % 7])
    turtle.width(i/100 + 1)
    turtle.forward(i)
    turtle.left(59)


turtle.hideturtle()

turtle.done()