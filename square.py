import turtle
t = turtle.Turtle()
t.color("white")
t.shape("turtle")
wn = turtle.Screen()
wn.bgcolor("black")
t.speed(1)
t.begin_fill()
t.fillcolor("red")

for i in range(4):
    t.forward(150)
    t.left(90)

t.end_fill()
t.hideturtle()
