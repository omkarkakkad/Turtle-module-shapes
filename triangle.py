import turtle
t = turtle.Turtle()
t.color("white")
t.shape("turtle")
wn = turtle.Screen()
wn.bgcolor("black")
t.speed(1)
t.begin_fill()
t.fillcolor("green")

t.circle(100, steps=3)


t.end_fill()
t.hideturtle()
